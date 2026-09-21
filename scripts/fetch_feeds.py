#!/usr/bin/env python3
"""自動抓取期刊新文章（CrossRef ＋ RSS），寫入 feeds.csv 給 Scanner 當起點。

只抓、只做關鍵字粗篩，不做任何判斷。人工來源（criticalcarereviews、會議）由 Scanner 另外處理。
只用 Python 標準函式庫，不需安裝套件（Python 3.11+）。

用法：
  python scripts/fetch_feeds.py critical-care 2026-W38 --since 2026-09-10
"""
import argparse, csv, datetime, json, pathlib, re, sys, tomllib, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from schema import FEEDS

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "pulm-evidence-digest/1.0 (mailto:{email})"


def get(url, email, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA.format(email=email)})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def crossref(src, since, email):
    params = {
        "filter": f"issn:{src['issn']},from-pub-date:{since}",
        "rows": str(src.get("max_items", 40)),
        "select": "DOI,title,published,type,URL",
        "sort": "published", "order": "desc", "mailto": email,
    }
    data = json.loads(get("https://api.crossref.org/works?" + urllib.parse.urlencode(params), email))
    for it in data["message"]["items"]:
        if it.get("type") not in (None, "journal-article"):
            continue
        parts = (it.get("published") or {}).get("date-parts", [[None]])[0]
        date = "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parts) if p)
        yield {"title": " ".join(it.get("title") or [""]), "url": it.get("URL", ""),
               "doi": it.get("DOI", ""), "pub_date": date}


def rss(src, since, email):
    root = ET.fromstring(get(src["url"], email))
    ns = {"a": "http://www.w3.org/2005/Atom", "dc": "http://purl.org/dc/elements/1.1/"}
    items = root.findall(".//item") or root.findall(".//a:entry", ns)
    for it in items:
        title = (it.findtext("title") or it.findtext("a:title", namespaces=ns) or "").strip()
        link = it.findtext("link") or ""
        if not link:
            el = it.find("a:link", ns)
            link = el.get("href", "") if el is not None else ""
        date = it.findtext("pubDate") or it.findtext("dc:date", namespaces=ns) or it.findtext("a:updated", namespaces=ns) or ""
        doi = it.findtext("dc:identifier", namespaces=ns) or ""
        m = re.search(r"10\.\d{4,9}/\S+", doi + " " + link)
        yield {"title": title, "url": link.strip(), "doi": m.group(0) if m else "", "pub_date": date.strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("domain"); ap.add_argument("week")
    ap.add_argument("--since", default=(datetime.date.today() - datetime.timedelta(days=8)).isoformat())
    a = ap.parse_args()

    cfg = tomllib.loads((ROOT / "domains" / a.domain / "sources.toml").read_text(encoding="utf-8"))
    email = cfg["contact_email"]
    kws = [k.lower() for k in cfg["filter"]["keywords"]]
    noise = re.compile(cfg["filter"].get("noise_regex", r"^$"), re.I)

    out = ROOT / "data" / a.domain / "work" / a.week / "feeds.csv"
    if not out.parent.exists():
        sys.exit(f"先執行：python scripts/new_week.py {a.domain} {a.week}")

    rows, seen, n = [], set(), 0
    for kind, fn in (("crossref", crossref), ("rss", rss)):
        for src in cfg.get(kind, []):
            try:
                got = kept = 0
                for it in fn(src, a.since, email):
                    got += 1
                    t = it["title"].lower()
                    if noise.search(t):
                        continue
                    hits = [k for k in kws if k in t]
                    if src.get("filter", False) and not hits:
                        continue
                    key = it["doi"].lower() or t
                    if key in seen:
                        continue
                    seen.add(key); n += 1; kept += 1
                    rows.append({"feed_id": f"F{n:03d}", "source": src["name"], **it,
                                 "matched_keywords": ";".join(hits)})
                flag = "  ⚠️ 0 筆：檢查 ISSN／URL" if got == 0 else ""
                print(f"{src['name']:<40} 抓 {got:>3}｜留 {kept:>3}{flag}")
            except Exception as e:
                print(f"{src['name']:<40} 失敗：{e}")

    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FEEDS); w.writeheader(); w.writerows(rows)
    print(f"\n共 {len(rows)} 筆 → {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
