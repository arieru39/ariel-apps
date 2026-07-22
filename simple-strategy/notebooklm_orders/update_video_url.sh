#!/bin/bash
#
# Simple Strategy NotebookLM 発注書 — 生成した動画の YouTube URL を data.json に反映
#
# 使い方:
#   bash update_video_url.sh <lo_id> <youtube_embed_url>
#
# 例:
#   bash update_video_url.sh creating_space https://www.youtube.com/embed/dQw4w9WgXcQ
#   bash update_video_url.sh meta https://www.youtube.com/embed/xxx  # メタ動画は book.playlist_embed_url に入る
#
# 動作:
#   1. data.json の該当テーマの video_embed_url を更新
#   2. state.json の該当LOを done に
#   3. git add / commit / push（自動デプロイ）

set -euo pipefail

export LANG="${LANG:-en_US.UTF-8}"
export LC_CTYPE="${LC_CTYPE:-en_US.UTF-8}"

DIR="$(cd "$(dirname "$0")" && pwd)"
APP_DIR="$(cd "$DIR/.." && pwd)"
DATA_JSON="$APP_DIR/data.json"
STATE="$DIR/state.json"
MANIFEST="$DIR/manifest.json"

if [ $# -lt 2 ]; then
  echo "使い方: bash update_video_url.sh <lo_id> <youtube_embed_url>" >&2
  echo "" >&2
  echo "例:" >&2
  echo "  bash update_video_url.sh creating_space https://www.youtube.com/embed/xxxxx" >&2
  exit 1
fi

LO_ID="$1"
URL="$2"

# URL を埋め込み形式に正規化
if [[ "$URL" =~ ^https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]+) ]]; then
  VIDEO_ID="${BASH_REMATCH[1]}"
  URL="https://www.youtube.com/embed/$VIDEO_ID"
  echo "ℹ️  watch URL を embed URL に変換: $URL"
elif [[ "$URL" =~ ^https://youtu\.be/([A-Za-z0-9_-]+) ]]; then
  VIDEO_ID="${BASH_REMATCH[1]}"
  URL="https://www.youtube.com/embed/$VIDEO_ID"
  echo "ℹ️  youtu.be URL を embed URL に変換: $URL"
fi

if [[ ! "$URL" =~ ^https://www\.youtube\.com/embed/ ]]; then
  echo "⚠️  URL が YouTube 埋め込み形式ではありません: $URL" >&2
  echo "   期待する形式: https://www.youtube.com/embed/<VIDEO_ID>" >&2
  read -p "   このまま進めますか? [y/N] " ans
  if [ "$ans" != "y" ]; then
    exit 1
  fi
fi

# data.json を更新
python3 << PYEOF
import json
from pathlib import Path

data_path = Path("$DATA_JSON")
data = json.loads(data_path.read_text(encoding="utf-8"))

lo_id = "$LO_ID"
url = "$URL"

if lo_id == "meta":
    # メタ動画は book.playlist_embed_url に入れる
    data.setdefault("book", {})["playlist_embed_url"] = url
    data["book"]["playlist_title"] = "全体像のルーブリックと11のLO — 対話式解説"
    print(f"✅ book.playlist_embed_url を更新: {url}")
else:
    found = False
    for theme in data.get("themes", []):
        if theme.get("id") == lo_id:
            theme["video_embed_url"] = url
            if not theme.get("video_title"):
                theme["video_title"] = f"{theme.get('title', lo_id)} — 対話式解説"
            found = True
            print(f"✅ themes[{lo_id}].video_embed_url を更新: {url}")
            break
    if not found:
        print(f"❌ themes に id={lo_id} が見つかりません")
        raise SystemExit(1)

data_path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)
PYEOF

# JSON 構文検証
python3 -c "import json; json.load(open('$DATA_JSON'))" && echo "✅ data.json 構文 OK"

# state.json を更新
python3 << PYEOF
import json, datetime
from pathlib import Path
state_path = Path("$STATE")
state = json.loads(state_path.read_text(encoding="utf-8"))
if "$LO_ID" in state:
    state["$LO_ID"]["status"] = "done"
    state["$LO_ID"]["video_url"] = "$URL"
    state["$LO_ID"]["generated_at"] = datetime.datetime.now().isoformat()
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("✅ state.json 更新")
PYEOF

# git commit & push
cd "$APP_DIR/.."
git add "simple-strategy/data.json" "simple-strategy/notebooklm_orders/state.json"
git commit -m "simple-strategy: set video URL for $LO_ID

$URL"
git push
echo ""
echo "🚀 デプロイ完了。1〜3分で反映されます:"
echo "   https://arieru39.github.io/ariel-apps/simple-strategy/"

# 進捗を表示
echo ""
python3 << PYEOF
import json
m = json.load(open("$MANIFEST"))
s = json.load(open("$STATE"))
done = sum(1 for v in m["videos"] if s.get(v["id"], {}).get("status") == "done")
total = len(m["videos"])
print(f"📊 進捗: {done}/{total} 完了")
if done < total:
    remaining = [v for v in m["videos"] if s.get(v["id"], {}).get("status") != "done"]
    print(f"⏳ 残り: {', '.join(v['id'] for v in remaining[:3])}{'...' if len(remaining) > 3 else ''}")
    print(f"   次: bash paste_prompt.sh next")
PYEOF
