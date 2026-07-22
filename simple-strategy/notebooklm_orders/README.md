# Simple Strategy — NotebookLM 発注書パイプライン

Simple Strategy 学習アプリの **12本の動画**（メタ1本 + LO 11本）を、NotebookLM の Audio/Video Overview で生成 → YouTube アップ → アプリ反映まで、**片手で回せる** 発注書パイプライン。

## 全体像

```
[原本プロンプト.md]
      ↓ _extract_orders.py
[12個の発注書 .md] + manifest.json + state.json
      ↓ paste_prompt.sh <lo_id>
[クリップボードに Customize プロンプト]
      ↓ NotebookLM に貼る（手動）
[動画生成 → ダウンロード → YouTube 非公開アップ]
      ↓ update_video_url.sh <lo_id> <youtube_url>
[data.json 更新 → git commit → push → GitHub Pages 反映]
```

## ファイル構成

| ファイル | 役割 |
|---|---|
| `_extract_orders.py` | 原本プロンプトmdを12本の発注書に分割（1回だけ実行すればOK） |
| `manifest.json` | 12動画のメタデータ索引（自動生成） |
| `state.json` | 進捗管理（pending / in_progress / done） |
| `paste_prompt.sh` | Customize プロンプトをクリップボードにコピー |
| `update_video_url.sh` | 生成後のYouTube URLをdata.jsonに反映＋自動デプロイ |
| `00_meta_全体像.md` 〜 `11_rapid_experimentation.md` | 各動画の発注書 |

## 使い方

### 準備（初回のみ）

```bash
cd /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders
python3 _extract_orders.py
```

これで12個の発注書と `manifest.json` / `state.json` が生成される。

### 進捗確認

```bash
bash paste_prompt.sh list
```

出力例：
```
📊 進捗一覧
======================================================================
✅ 00 [meta] meta                           全体像のルーブリックと11のLO → https://...
🎬 01 [L1] creating_space                 空間をつくる
⏳ 02 [L1] calm_mindset                   穏やかな心
...
```

### 1本ずつ回す

#### Step 1. 次の動画のプロンプトをクリップボードへ

```bash
# 特定のLOを指定
bash paste_prompt.sh creating_space

# または、次の pending を自動で選ぶ
bash paste_prompt.sh next
```

すると：
- Customize プロンプトがクリップボードにコピーされる
- どの Notebook を作ればいいか、どの Source をアップすればいいかが表示される
- state.json のステータスが `in_progress` になる

#### Step 2. NotebookLM で動画を生成（手動）

1. https://notebooklm.google.com/ を開く
2. 「新規 Notebook」を作成（名前は表示された通り、例：`ariel-apps/simple-strategy/creating_space`）
3. Sources に以下の2件をアップロード：
   - `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
   - `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`
4. Studio → Video Overview → Customize を開く
5. **Cmd+V で貼り付け**（クリップボードに入っている）
6. Generate → 完成したら MP4/MP3 をダウンロード

#### Step 3. YouTube にアップして埋め込みURLを取得

1. YouTube Studio で「非公開」アップロード
2. 動画URLをコピー（`https://youtu.be/xxx` または `https://www.youtube.com/watch?v=xxx` のいずれでもOK。スクリプトが自動で `embed` 形式に変換する）

#### Step 4. アプリに反映して自動デプロイ

```bash
bash update_video_url.sh creating_space https://youtu.be/xxxxx
```

これで：
- `data.json` の該当テーマの `video_embed_url` が更新される
- `state.json` の該当LOが `done` になる
- git add / commit / push が自動実行される
- GitHub Actions が GitHub Pages にデプロイ（1〜3分）
- https://arieru39.github.io/ariel-apps/simple-strategy/ で反映確認

### メタ動画（動画00）の扱い

メタ動画は個別テーマではないので、`data.json` の `book.playlist_embed_url` に格納される：

```bash
bash update_video_url.sh meta https://youtu.be/xxxxx
```

## 想定所要時間（1本あたり）

| ステップ | 時間 |
|---|---|
| クリップボード取得 | 5秒 |
| NotebookLM で動画生成 | 5〜10分 |
| ダウンロード + YouTubeアップ | 5〜10分 |
| `update_video_url.sh` 実行 | 30秒 |
| **合計** | **10〜20分/本 × 12本 = 2〜4時間** |

## 自動化されていない部分

以下は **意図的に手動** にしている（信頼性と柔軟性のため）：

1. **NotebookLM の操作**：ブラウザ自動化はNotebookLMのUI変更に弱く、動画生成の完了待ちが不安定
2. **YouTube アップロード**：非公開/公開の判定、サムネイル選択、タイトル微調整は手動が確実
3. **Sources のアップロード**：NotebookLM側でファイル選択ダイアログが出るので、そこだけ手動

## トラブル対処

### 「LO not found」と表示される

`_extract_orders.py` を再実行して `manifest.json` を作り直す：
```bash
python3 _extract_orders.py
```

### クリップボードに何も入らない（macOS）

ロケール未設定の環境で発生することがある。以下を実行してから再試行：
```bash
export LANG=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8
bash paste_prompt.sh <lo_id>
```

（スクリプト冒頭で自動 export しているので通常は不要）

### `update_video_url.sh` で git push に失敗する

`~/Workspace/ariel-apps/` で手動で確認：
```bash
cd ~/Workspace/ariel-apps
git status
git pull --rebase
git push
```

### state.json をリセットしたい

```bash
python3 -c "
import json
from pathlib import Path
p = Path('state.json')
s = json.loads(p.read_text(encoding='utf-8'))
for v in s.values():
    v['status'] = 'pending'
    v['video_url'] = None
    v['generated_at'] = None
p.write_text(json.dumps(s, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
"
```

## 原本プロンプトの場所

- **[[プロンプト_学習アプリのLO動画をNotebookLMでつくる_SimpleStrategy]]**
- 絶対パス: `/Users/suzukitoshikazux/ありえるObsidian/07プロンプト/プロンプト/プロンプト_学習アプリのLO動画をNotebookLMでつくる_SimpleStrategy.md`

原本を編集した後は `python3 _extract_orders.py` を再実行して発注書を更新すること。
