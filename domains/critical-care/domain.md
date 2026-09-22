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

## 收錄範圍（族群）
- 只收**成人（≥18 歲）**。
- **Scanner 預篩**：標題或摘要明確以下列族群為主者，照列入 candidates，但 `note` 以 `SKIP:PEDIATRIC` 開頭：
  pediatric、paediatric、PICU、neonatal、NICU、preterm、infant、children、adolescent
- **不預篩、交 Curator 判斷**：年齡涵蓋兒童與成人者；標題未說明年齡者；納入條件為 ≥16 歲者。
- **Curator 判斷規則**：
  - 全部受試者 <18 歲 → 排除，`PEDIATRIC`
  - 混合年齡且有成人分層結果 → 收錄，`population` 註明「成人分層」，數字只取成人分層
  - 混合年齡、無分層、以成人為主（如 ≥16 歲入組）→ 收錄
  - 混合年齡、無分層、以兒童為主 → 排除，`PEDIATRIC`
  - Guideline 同時涵蓋兒童與成人 → 收錄，只摘成人部分

## 收錄範圍（臨床情境）
- 聚焦**內科加護病房**、內科重症病人的照護。
- **預篩略過（照列，note 標 `SKIP:OUT_OF_SCOPE`）**：麻醉與術中管理、手術前後照護（心臟、腹部、胸腔等術後 ICU）、手術術式或技術比較、外傷（含 TBI）、燒傷。
- **例外，保留**：lung transplantation 術後的內科照護（PGD、排斥、感染、免疫抑制、呼吸器脫離、ECMO bridge）。**不含**任何術式或手術技術的探討。
- **不預篩、交 Curator**：內外科混合 ICU 的研究（多數大型 ICU 試驗屬此類）。Curator 判斷：以內科病人為主或有內科分層 → 收錄；以術後病人為主 → 排除，`OUT_OF_SCOPE`。

## 收錄門檻（證據等級）
目標：只收**臨床上可直接使用**的證據。Scanner 依**研究設計**判斷，不需確認樣本數；規模由 Verifier 記錄、Curator 判斷。

**通過（進主清單）**，符合任一：
- **RCT**：任何規模（pilot／feasibility 除外）
- **Systematic review／meta-analysis**：全部通過
- **Guideline**：國際或主要學會正式發布的指引、focused update、官方 consensus／clinical practice statement（例：Surviving Sepsis Campaign、ESICM／ATS ARDS guideline、SCCM、ERS、KDIGO）
- **大型觀察性研究**：n ≥ 5,000，或全國／多國資料庫（這一類才需要從摘要確認 n）
- **Narrative review**：通過（重點整理用途）。受 Curator 每節上限約束
- **watchlist 試驗**：有新結果即通過

**摘要抓不到時**（rate limit、付費牆、頁面錯誤）：**不得 SKIP**。照列主清單，note 以 `CHECK:未取得摘要` 開頭，交 Verifier 查證。SKIP 只能用在「確認不符合」，不能用在「沒查到」。

**預篩略過（照列，note 標 `SKIP:LOW_EVIDENCE`）**：
pilot／feasibility RCT、post hoc／secondary analysis、小型或單中心觀察性研究、physiology／crossover 研究、protocol 論文、case series

**不列入 candidates（非研究文章）**：
editorial、commentary、correspondence／letter、case report

**Curator 端上限**：每節最多 4 筆；超過依 practice_impact 排序，其餘標 LOW_PRIORITY
**排除代碼**：`OUT_OF_SCOPE` / `DUPLICATE` / `LOW_PRIORITY` / `UNVERIFIED` / `PRECLINICAL` / `SINGLE_CENTER_SMALL` / `PEDIATRIC` / `LOW_EVIDENCE`

## Verifier 欄位補充
- `population` 必含**年齡範圍**（納入條件或實際中位數／範圍）
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
