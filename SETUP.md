# 建立 repo（一次性，約 15 分鐘）

1. GitHub 右上角 **+ → New repository**
   - 名稱：`pulm-evidence-digest`（可自訂）
   - Visibility：Public 或 Private 皆可。注意：**Private repo 的 Wiki 需要付費方案（GitHub Pro）**；不要 Wiki 就不影響。
   - 不勾選任何初始化選項
2. 解壓縮 zip，用 GitHub 網頁的 **uploading an existing file** 把整個資料夾內容拖進去（含 `.claude`、`.github` 隱藏資料夾；網頁上傳若看不到隱藏資料夾，改用 GitHub Desktop）。
3. 編輯 `domains/critical-care/sources.toml`，把 `contact_email` 改成妳的 email。
4. （要 Wiki 的話）到 repo 的 **Wiki** 分頁建立第一頁，內容隨意。
5. 舊 repo `thoracic-uptodate`：Settings → 最下方 **Archive this repository**。保留唯讀，不刪除。

之後：第 0 階段看 `docs/claude-ai-mode.md`；要搬 Claude Code 時，在本機 clone 這個 repo，於資料夾內啟動 Claude Code 即可，角色會自動被辨識。

## 腳本需求
Python 3.11 以上，不需安裝任何套件。只在 Claude Code 階段或妳自己想在本機跑時才需要。
