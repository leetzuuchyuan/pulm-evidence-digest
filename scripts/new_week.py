#!/usr/bin/env python3
"""建立本週工作資料夾與空白 CSV 表頭。

用法：
  python scripts/new_week.py critical-care            # 本週
  python scripts/new_week.py critical-care 2026-W39   # 指定週次
"""
import csv, datetime, pathlib, sys
from schema import CANDIDATES, EVIDENCE, FEEDS

ROOT = pathlib.Path(__file__).resolve().parent.parent


def iso_week(d=None):
    y, w, _ = (d or datetime.date.today()).isocalendar()
    return f"{y}-W{w:02d}"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    domain = sys.argv[1]
    week = sys.argv[2] if len(sys.argv) > 2 else iso_week()
    if not (ROOT / "domains" / domain / "domain.md").exists():
        sys.exit(f"找不到 domains/{domain}/domain.md")
    wd = ROOT / "data" / domain / "work" / week
    wd.mkdir(parents=True, exist_ok=True)
    for name, cols in [("feeds.csv", FEEDS), ("candidates.csv", CANDIDATES), ("evidence.csv", EVIDENCE)]:
        p = wd / name
        if p.exists():
            print(f"已存在，略過：{p.relative_to(ROOT)}")
            continue
        with p.open("w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(cols)
        print(f"建立：{p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
