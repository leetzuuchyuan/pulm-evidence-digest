#!/usr/bin/env python3
"""機械檢查 evidence.csv。Verifier、Curator 交件前各跑一次；Auditor 開工前再跑一次。

用法：python scripts/validate_evidence.py critical-care 2026-W38 [--stage verifier|curator]
結束代碼 0 = 通過，1 = 有錯。
"""
import argparse, csv, pathlib, re, sys
from schema import EVIDENCE, EVIDENCE_A, EVIDENCE_B, EVIDENCE_C, ENUMS

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOI = re.compile(r"^10\.\d{4,9}/\S+$")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("domain"); ap.add_argument("week")
    ap.add_argument("--stage", choices=["verifier", "curator"], default="curator")
    a = ap.parse_args()
    p = ROOT / "data" / a.domain / "work" / a.week / "evidence.csv"
    rows = list(csv.DictReader(p.open(encoding="utf-8-sig")))
    errs = []

    header = next(csv.reader(p.open(encoding="utf-8-sig")))
    if header != EVIDENCE:
        errs.append("表頭與 scripts/schema.py 不一致")

    for r in rows:
        cid = r.get("candidate_id", "?")
        for c in EVIDENCE_A + EVIDENCE_B:
            if not (r.get(c) or "").strip():
                errs.append(f"{cid}: {c} 空白（查過沒有請填 NR）")
        if r.get("doi") not in ("", "NR") and not DOI.match(r["doi"]):
            errs.append(f"{cid}: DOI 格式錯誤 → {r['doi']}")
        if r.get("evidence_level") and r["evidence_level"] not in ENUMS["evidence_level"]:
            errs.append(f"{cid}: evidence_level 非法值 → {r['evidence_level']}")
        if a.stage == "curator" and r.get("evidence_level") != "unverified":
            for c in ("status", "practice_impact"):
                v = r.get(c, "")
                if v and v not in ENUMS[c]:
                    errs.append(f"{cid}: {c} 非法值 → {v}")
            if r.get("evidence_level") == "abstract-only" and r.get("practice_impact") == "改變":
                errs.append(f"{cid}: abstract-only 不得標 practice_impact=改變")

    print(f"{p.relative_to(ROOT)}：{len(rows)} 列，{len(errs)} 個問題")
    for e in errs:
        print("  -", e)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
