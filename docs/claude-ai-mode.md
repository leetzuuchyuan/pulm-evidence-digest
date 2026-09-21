# Claude.ai 手動執行（第 0 階段）

目的：在不裝任何工具的情況下，先驗證角色切分是否真的減輕負擔。

## 一次性設定

1. 新建 Project「重症週報 v2」。
2. Project instructions 貼入 `domains/critical-care/domain.md` 全文。
3. **不要**把角色檔放進 Project instructions 或 knowledge。
4. 舊的重症週報 Project 改名為「重症週報（存檔）」，不再寫入。

## 每週

在「重症週報 v2」裡依序開五個 chat，標題 `W38 scanner`、`W38 verifier`……

每個 chat 的第一則訊息：

```
<貼上 .claude/agents/<角色>.md 的全文>

---
domain: critical-care
week: 2026-W38
掃描起始日: 2026-09-10
<貼上上一關的輸出檔內容；Scanner 則貼 watchlist.toml>
```

角色檔提到「執行 validate_evidence.py」的步驟，在 Claude.ai 裡改為請它「依 scripts/schema.py 的規則自我檢查後回報」，或把 evidence.csv 貼到下一關前自己用 Excel 看一眼有沒有空格。

每關產出存回 repo 對應位置（GitHub 網頁版可直接新增／編輯檔案）。

## 第一週跑完記錄

| 關卡 | 花費分鐘 | 最卡的地方 |
|---|---|---|
| scanner | | |
| verifier | | |
| curator | | |
| writer | | |
| auditor | | |

這張表決定下一步：值得搬 Claude Code、需要改角色，或回到原本做法。
