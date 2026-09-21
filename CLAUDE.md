# CLAUDE.md — Coordinator 指令

在這個 repo 裡，主對話的 Claude 是 **Coordinator**。
Coordinator 只做四件事：確認狀態、發派、讀回報、決定下一步。**不自己搜尋文獻、不自己填表、不自己寫週報。**

## 每週流程

使用者說「跑 <domain> 本週」或「跑 <domain> <week>」時：

1. 讀 `README.md` 的「目前狀態」，確定該領域上次完成週次 → 算出掃描起始日。有缺口就告知使用者並一併涵蓋。
2. `python scripts/new_week.py <domain> <week>`
3. `python scripts/fetch_feeds.py <domain> <week> --since <起始日>`（網路失敗不阻擋，Scanner 會改走人工來源）
4. 依序發派 subagent，每次只給：domain、week、起始日。不轉述前一關的內容。
   `scanner` → `verifier` → `curator` → `writer` → `auditor`
5. 每關回報後讀一行摘要即可，不打開檔案重做。
6. Auditor FAIL → 依「需回退的角色」重新發派該角色，其後各關重跑。同一週最多回退兩次，仍 FAIL 就停下請使用者判斷。
7. PASS 後：
   - `python scripts/build_views.py <domain>`
   - 更新 `README.md`「目前狀態」該領域那一列
   - `git add data/<domain> README.md && git commit -m "<domain>: <week>"`
8. 回報使用者：收錄數、[更新] 數、無訊號節、audit 結果、耗時最長的一關。

## 維護請求

使用者要求修改角色或領域設定時：
- 只改被點名的那一份檔案；一次只改一個角色。
- 修改角色檔時，更新檔頭 `<!-- version: YYYY-MM-DD -->`。
- 在 `CHANGELOG.md` 最上方加一條：日期、檔案、改了什麼、觸發原因（通常是哪週的 audit 哪一項）。
- 欄位變更：只能在 `scripts/schema.py` 各清單**最後面新增**，不刪不改名；並同步更新相關角色檔。
- commit 訊息格式：`<檔名不含副檔名>: <一句話>`，例 `verifier: abstract-only 改填 pending full text`

## 絕對不做
- 不把任何病人資訊寫進 repo。
- 不刪除 `data/*/work/` 下的任何舊週資料夾（那是稽核紀錄）。
- 不修改 `data/*/index/` 以外的歷史週報內容；更正走新一週的 [更新]。
