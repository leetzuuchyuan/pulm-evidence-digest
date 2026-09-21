# pulm-evidence-digest

胸腔／重症醫學每週文獻更新的多角色工作流程與在地資料庫。

一句話：**五個互不污染的角色，透過檔案交接；角色跨領域共用，領域只換設定檔。**

## 目前狀態

| 領域 | 最後完成週次 | 缺口 | 備註 |
|---|---|---|---|
| critical-care | — | — | 首次執行；舊週報待回填（見 docs/migrator.md） |

## 結構

```
.claude/agents/        五個角色（跨領域共用，Claude Code subagent 格式）
  scanner  verifier  curator  writer  auditor
domains/
  critical-care/       domain.md（規則）· sources.toml（自動來源）· watchlist.toml（追蹤試驗）
  _template/           新領域從這裡複製
data/<domain>/
  work/<YYYY-Www>/     feeds → candidates → evidence → outline → audit（每週一夾，永不刪）
  reports/             成品週報（push 後自動發布到 Wiki）
  index/trials.csv     累積索引：收錄過的試驗，[更新] 判斷依據
  index/excluded.csv   排除紀錄＋理由
  views/               由 build_views.py 產生：citations.bib（手稿）· teaching.md（教學）
scripts/               schema（欄位唯一定義）· new_week · fetch_feeds · validate_evidence · build_views
docs/                  claude-ai-mode（手動版操作）· migrator（舊週報回填）
CLAUDE.md              Coordinator 指令
CHANGELOG.md           角色與設定的修改紀錄
```

## 流程

```
fetch_feeds.py ─▶ Scanner ─▶ Verifier ─▶ Curator ─▶ Writer ─▶ Auditor
   feeds.csv    candidates   evidence   outline    週報.md    audit.md
                             (A,B,D組)  (C組+索引)  (不上網)   (唯讀)
```

三條鐵律：Coordinator 不做實質工作；角色之間只透過檔案交接；每個角色只寫自己的檔案。

## 兩種執行方式

| | Claude.ai（手動） | Claude Code |
|---|---|---|
| Coordinator | 妳自己 | 主對話的 Claude |
| 角色 | 每關開一個新 chat，貼入角色檔 | subagent 自動發派 |
| 檔案 | 手動存回 repo | 直接讀寫、commit |
| 腳本 | 不需要 | 自動執行 |
| 說明 | `docs/claude-ai-mode.md` | 在 repo 資料夾開 Claude Code，說「跑 critical-care 本週」 |

## 維護

- **只依 audit.md 改東西。** 同一項連續兩週 FAIL 才動手，一週只改一個角色。
- 改完在 `CHANGELOG.md` 記一條，commit 訊息 `<檔名>: <改了什麼>`。
- 欄位只在 `scripts/schema.py` 最後面新增，不刪不改名。
- 新增領域：複製 `domains/_template/`，改三個設定檔，建 `data/<slug>/index/` 兩個 CSV。

## 隱私

本 repo 不存放任何病人資訊。`local_applicability` 只寫制度層級（健保、藥品可取得性、流程差異）。

## 來歷

架構概念參考自先前 fork 的 thoracic-uptodate（原作者 htlin222 的 breast-cancer-uptodate）：「領域知識放設定檔、不改程式」與「reports 推送後自動發布 Wiki」兩個想法。原 repo 未附授權條款，因此本 repo 的程式與文件均為重新撰寫，未複製原始碼。期刊 ISSN 與 RSS 網址為公開事實資訊。
