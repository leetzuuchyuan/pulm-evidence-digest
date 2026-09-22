# CHANGELOG

格式：`## YYYY-MM-DD` → `- <檔案>：<改了什麼>（觸發：<哪週 audit 哪一項 / 其他原因>）`
最新的寫在最上面。

## 2026-09-22
- domain.md（critical-care）：narrative review 改為通過（重點整理用途），不再列於「不列入」；item_type 新增 narrative-review（schema.py、scanner.md v2026-09-22c）；writer.md（v2026-09-22）新增 review 條目格式（觸發：使用者決定，review 常為重點整理）
- domain.md（critical-care）：證據門檻改為依研究設計判斷——RCT 任何規模、SR／MA 全部通過，只有大型觀察性研究需確認 n；摘要抓不到時改標 CHECK 不得 SKIP；narrative review 等非研究文章改為「不列入」（觸發：W38 scanner v3 主清單僅 3 筆，7 筆因 rate limit 被誤判 LOW_EVIDENCE；scanner 回報規則 1 與預篩清單衝突）
- scanner.md（v2026-09-22b）：主清單加 note 欄顯示 CHECK；規則 1 改依 domain.md「不列入」清單
- domain.md（critical-care）：新增「收錄範圍（臨床情境）」聚焦內科 ICU，手術相關以 SKIP:OUT_OF_SCOPE 預篩，保留 lung transplantation 術後內科照護；證據門檻新增「須從摘要確認」（觸發：W38 scanner v2 主清單 37 筆，含術後研究）
- watchlist.toml：移除 PROSPECT（原主題填寫錯誤；同名 PROSpect 為兒科試驗）（觸發：W38 scanner 回報）
- scanner.md、verifier.md、curator.md（v2026-09-22）：欄位順序改參照 context 的 schema.md；CSV 改為可下載檔案（UTF-8 BOM）（觸發：Claude.ai 看不到 scripts/schema.py；CSV 在對話中難讀）
- docs/schema.md＋scripts/export_schema_md.py：新增，供 Claude.ai Context 使用
- build_views.py、validate_evidence.py：讀檔改 utf-8-sig，相容 BOM

## 2026-09-21
- domain.md（critical-care）：「收錄門檻與上限」改為「收錄門檻（證據等級）」，定義 RCT／guideline／大型研究的通過條件，其餘以 SKIP:LOW_EVIDENCE 預篩；新增排除代碼 LOW_EVIDENCE（觸發：W38 scanner 50 筆過多，只要臨床可用的高等級證據）
- scanner.md（v2026-09-21c）：對話中只呈現主清單（非 SKIP），SKIP 改為一行計數；完整 CSV 照舊保留
- scanner.md（v2026-09-21b）：新增「對話中的呈現順序」，交件時先給統計表、來源覆蓋、分組清單，再給完整 CSV（觸發：W38 scanner 50 筆原始 CSV 難以閱讀）
- domain.md（critical-care）：新增「收錄範圍」只收成人 ≥18 歲；新增排除代碼 PEDIATRIC；population 必含年齡範圍（觸發：W38 scanner 測試，範圍決策）
- scanner.md：新增規則 6，預篩條目照列並以 `SKIP:<代碼>` 標註；回報行加 SKIP 數
- verifier.md：新增規則 5，SKIP 列不查證
- curator.md：輸入加 candidates.csv；新增規則 3、4 處理 SKIP 列與族群判斷

## 2026-09-18
- 全部：初版建立。五角色、critical-care 領域、schema v1、四支腳本。
