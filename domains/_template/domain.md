> **範本**：複製整個 `domains/_template/` 為 `domains/<slug>/`，改寫本檔、`sources.toml`、`watchlist.toml`；
> 建立 `data/<slug>/index/trials.csv`、`excluded.csv`（表頭見 scripts/schema.py）後，用 new_week.py 開始。
> 以下內容為重症版範例，請整份改寫。`.claude/agents/` 一字不改。

# 領域設定：重症醫學（critical-care）

所有角色執行時一併載入本檔。角色邏輯在 `.claude/agents/`，本檔只放領域專屬設定。
相關檔案：`sources.toml`（自動抓取來源）、`watchlist.toml`（追蹤中試驗）。

## 週報名稱與檔名
- 標題：`🏥 重症醫學趨勢週報 — YYYY-Www`
- 檔名：`data/critical-care/reports/重症醫學趨勢週報_YYYY-Www.md`

## Scanner 來源順位
1. `feeds.csv`（scripts/fetch_feeds.py 自動抓取的期刊新文章；若本週未執行則略過）
2. criticalcarereviews.com/latest-evidence/journal-watch（近期 e-pub 試驗清單）
3. `watchlist.toml` 每個試驗縮寫逐一精準搜尋
4. 以第 2 步取得的試驗縮寫逐一精準搜尋
5. 主要會議摘要（ESICM LIVES、SCCM Congress、ATS、ISICEM）→ item_type 標 conference-abstract

已知不可用：UpToDate What's New（JS／登入牆），不要嘗試。
搜尋原則：試驗縮寫或會議名＋年分的精準搜尋，勝過期刊層級的廣泛搜尋。

## 分節（section 編號）
1. 🫁 ARDS — 機械通氣策略（driving pressure / PEEP / tidal volume / prone）
2. 🧬 ARDS — Subphenotype 與精準治療（hyper- vs hypoinflammatory / biomarker-guided）
3. 🦠 Sepsis（早期辨識 / 抗生素 / source control）
4. 💉 Vasopressor 與血流動力學（norepinephrine / vasopressin / angiotensin II / fluids）
5. 💊 ICU 用藥（corticosteroid / NMB / sedation / nutrition）
6. 🫀 ECMO（VV / VA / 適應症 / 撤機）
7. 📘 Guideline 更新（ATS / SCCM / ESICM）

## 收錄門檻與上限
- 收錄：RCT、guideline、對 practice 有影響的大型觀察性研究或 meta-analysis
- 每節上限 4 筆；超過依 practice_impact 排序
- 排除代碼：`OUT_OF_SCOPE` / `DUPLICATE` / `LOW_PRIORITY` / `UNVERIFIED` / `PRECLINICAL` / `SINGLE_CENTER_SMALL`

## Verifier 欄位補充
- `population` 必含適用嚴重度指標：APACHE II / SOFA / P/F ratio / 休克定義，擇一以上
- `primary_outcome` 優先：mortality（含時間點）、ventilator-free days、ICU LOS
- `effect_size` 優先：mortality 的 RR 或 absolute risk difference > HR > MD

## Curator 補充
- `local_applicability`：健保給付、國內可取得性、本院 ICU 現行流程差異。**不得寫入任何病人資訊。**

## 報告格式（Writer）
- 開頭 metadata 區塊：生成日期、涵蓋期間、資料來源
- `## 摘要：本週重點`（3–5 條，含數字）
- 若涵蓋多週：接一段「涵蓋期間說明」
- 依分節 1–7 順序，使用上方 emoji 標題
- 無收錄的節寫「本週無新訊號」
- 條目格式依 `.claude/agents/writer.md`
