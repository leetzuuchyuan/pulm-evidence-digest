# CHANGELOG

格式：`## YYYY-MM-DD` → `- <檔案>：<改了什麼>（觸發：<哪週 audit 哪一項 / 其他原因>）`
最新的寫在最上面。

## 2026-09-21
- domain.md（critical-care）：新增「收錄範圍」只收成人 ≥18 歲；新增排除代碼 PEDIATRIC；population 必含年齡範圍（觸發：W38 scanner 測試，範圍決策）
- scanner.md：新增規則 6，預篩條目照列並以 `SKIP:<代碼>` 標註；回報行加 SKIP 數
- verifier.md：新增規則 5，SKIP 列不查證
- curator.md：輸入加 candidates.csv；新增規則 3、4 處理 SKIP 列與族群判斷

## 2026-09-18
- 全部：初版建立。五角色、critical-care 領域、schema v1、四支腳本。
