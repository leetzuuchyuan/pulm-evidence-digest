#!/usr/bin/env python3
"""從歷週 evidence.csv 產生衍生檢視（只讀不改原始資料）。

  views/citations.bib    手稿引用（只收 audit_status=pass 且已收錄者）
  views/teaching.md      教學清單（practice_impact=改變 或 有 teaching_point）

用法：python scripts/build_views.py critical-care
"""
import csv, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    domain = sys.argv[1]
    base = ROOT / "data" / domain
    rows = []
    for p in sorted((base / "work").glob("*/evidence.csv")):
        rows += [r for r in csv.DictReader(p.open(encoding="utf-8-sig"))
                 if r.get("audit_status") == "pass" and r.get("section")]

    bib, seen, keys = [], set(), set()
    for r in rows:
        if r["doi"] in seen or r["doi"] == "NR":
            continue
        seen.add(r["doi"])
        key = re.sub(r"\W", "", (r["first_author"].split()[0] if r["first_author"] != "NR" else "anon")) + r["year"]
        key += re.sub(r"\W", "", r["trial_name"])[:12]
        base_key, i = key, 1
        while key in keys:
            i += 1; key = f"{base_key}{chr(96 + i)}"
        keys.add(key)
        bib.append(
            f"@article{{{key},\n  author = {{{r['first_author']}}},\n  title = {{{r['title_full']}}},\n"
            f"  journal = {{{r['journal_full']}}},\n  year = {{{r['year']}}},\n  doi = {{{r['doi']}}},\n"
            f"  note = {{{r['trial_name']}; PMID {r['pmid']}}}\n}}\n")
    (base / "views" / "citations.bib").write_text("\n".join(bib), encoding="utf-8")

    teach = [r for r in rows if r["practice_impact"] == "改變" or r["teaching_point"].strip()]
    lines = ["# 教學清單\n", "| 週次 | 試驗 | 臨床影響 | 一句話 | 可問住院醫師 | 引用 |", "|---|---|---|---|---|---|"]
    for r in sorted(teach, key=lambda r: r["week_id"], reverse=True):
        lines.append(f"| {r['week_id']} | {r['trial_name']} | {r['practice_impact']} | {r['takeaway_zh']} "
                     f"| {r['teaching_point']} | {r['journal_full']}, {r['year']}. doi:{r['doi']} |")
    (base / "views" / "teaching.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"citations.bib：{len(bib)} 筆；teaching.md：{len(teach)} 筆")


if __name__ == "__main__":
    main()
