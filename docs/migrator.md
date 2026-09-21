# 舊週報回填（一次性）

**時機：新流程成功跑完第一週之後。** 目的只是讓 `index/trials.csv` 有歷史，[更新] 判斷才有依據。這是抽取，不是重查。

## 做法

開一個 chat（或 Claude Code 對話），一次貼 1–3 份舊週報，加上以下指示：

```
你是 migrator。從以下舊週報中抽取每一個被報導的試驗，輸出 CSV，欄位：
trial_name,doi,first_seen_week,last_updated_week,section,status,practice_impact,takeaway_zh,previous_value

規則：
- 只抽取週報中明確寫出的內容，不上網、不補查。
- doi 週報沒寫就填 NR。
- first_seen_week 與 last_updated_week 都填該份週報的週次。
- section 依 domains/critical-care/domain.md 的分節編號對應；對不上填 ?。
- status 一律填「追蹤中」。
- practice_impact 填「待驗證」（舊資料未經新流程判讀）。
- takeaway_zh 用週報原文縮成 30 字內，保留一個數字。
- previous_value 留空。
- 同一試驗出現在多份週報：只保留一列，first_seen_week 取最早、last_updated_week 取最晚，takeaway 取最新。

<貼上舊週報>
```

輸出貼到 `data/critical-care/index/trials.csv` 表頭之下。
舊週報本身放到 `data/critical-care/reports/legacy/`，保持原檔名。
