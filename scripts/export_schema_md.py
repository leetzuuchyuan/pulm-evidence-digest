#!/usr/bin/env python3
"""由 scripts/schema.py 產生 docs/schema.md（給 Claude.ai Context 用）。改 schema.py 後執行一次。"""
import pathlib, schema
ROOT = pathlib.Path(__file__).resolve().parent.parent
blocks = [
    ("candidates.csv", "Scanner", schema.CANDIDATES),
    ("evidence.csv", "Verifier 填 A、B、D 組；Curator 填 C 組", schema.EVIDENCE),
    ("index/trials.csv", "Curator", schema.TRIALS_INDEX),
    ("index/excluded.csv", "Curator", schema.EXCLUDED),
]
out = ["# 欄位定義（自動產生，勿手改；來源 scripts/schema.py）\n",
       "規則：欄位順序固定；只在最後新增，不刪不改名。CSV 以 UTF-8 with BOM 存檔。\n"]
for name, who, cols in blocks:
    out += [f"## {name}（{who}）\n", "```", ",".join(cols), "```\n"]
out += ["## 列舉值\n"] + [f"- `{k}`：{' / '.join(sorted(v))}" for k, v in schema.ENUMS.items()]
(ROOT / "docs" / "schema.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("docs/schema.md updated")
