#!/bin/bash
#
# Simple Strategy NotebookLM 発注書 — Customize プロンプトをクリップボードにコピー
#
# 使い方:
#   bash paste_prompt.sh <lo_id>
#   bash paste_prompt.sh next        # state.json から次の pending を自動選択
#   bash paste_prompt.sh list        # 全 LO の状態を一覧
#
# 例:
#   bash paste_prompt.sh creating_space
#   bash paste_prompt.sh meta
#   bash paste_prompt.sh next

set -euo pipefail

# UTF-8 locale to ensure pbcopy/pbpaste handle Japanese correctly
export LANG="${LANG:-en_US.UTF-8}"
export LC_CTYPE="${LC_CTYPE:-en_US.UTF-8}"

DIR="$(cd "$(dirname "$0")" && pwd)"
MANIFEST="$DIR/manifest.json"
STATE="$DIR/state.json"

if [ ! -f "$MANIFEST" ]; then
  echo "❌ manifest.json が見つかりません: $MANIFEST" >&2
  echo "先に 'python3 $DIR/_extract_orders.py' を実行してください。" >&2
  exit 1
fi

TARGET="${1:-}"

if [ -z "$TARGET" ]; then
  echo "使い方: bash paste_prompt.sh <lo_id | next | list>"
  echo ""
  python3 -c "
import json
m = json.load(open('$MANIFEST'))
print('LO 一覧:')
for v in m['videos']:
    layer = f'L{v[\"layer\"]}' if v['layer'] else 'meta'
    print(f'  {v[\"seq\"]:02d} [{layer}] {v[\"id\"]:<30} — {v[\"title\"]}')"
  exit 0
fi

# list コマンド
if [ "$TARGET" = "list" ]; then
  python3 -c "
import json
m = json.load(open('$MANIFEST'))
s = json.load(open('$STATE'))
print('📊 進捗一覧')
print('='*70)
done = 0
for v in m['videos']:
    st = s.get(v['id'], {})
    status = st.get('status', 'pending')
    icon = '✅' if status == 'done' else ('🎬' if status == 'in_progress' else '⏳')
    url = st.get('video_url', '') or ''
    url_short = f' → {url[:40]}...' if url else ''
    layer = f'L{v[\"layer\"]}' if v['layer'] else 'meta'
    print(f'{icon} {v[\"seq\"]:02d} [{layer}] {v[\"id\"]:<30} {v[\"title\"]}{url_short}')
    if status == 'done':
        done += 1
print('='*70)
print(f'完了: {done}/{len(m[\"videos\"])}')"
  exit 0
fi

# next コマンド → state.json から次の pending を選ぶ
if [ "$TARGET" = "next" ]; then
  TARGET=$(python3 -c "
import json
m = json.load(open('$MANIFEST'))
s = json.load(open('$STATE'))
for v in m['videos']:
    st = s.get(v['id'], {})
    if st.get('status', 'pending') == 'pending':
        print(v['id'])
        break")
  if [ -z "$TARGET" ]; then
    echo "🎉 全 LO 完了しています！"
    exit 0
  fi
  echo "▶️  次の LO: $TARGET"
fi

# Customize プロンプトを取得してクリップボードへ
PROMPT=$(python3 -c "
import json
m = json.load(open('$MANIFEST'))
for v in m['videos']:
    if v['id'] == '$TARGET':
        print(v['customize_prompt'])
        break
else:
    import sys
    print('LO not found: $TARGET', file=sys.stderr)
    sys.exit(1)")

if [ -z "$PROMPT" ]; then
  echo "❌ LO '$TARGET' が見つかりません。" >&2
  echo "使える LO: bash paste_prompt.sh list" >&2
  exit 1
fi

# クリップボードにコピー
echo "$PROMPT" | pbcopy

# 状態を in_progress に更新
python3 -c "
import json, datetime
s = json.load(open('$STATE'))
if '$TARGET' in s:
    s['$TARGET']['status'] = 'in_progress'
    s['$TARGET']['started_at'] = datetime.datetime.now().isoformat()
    json.dump(s, open('$STATE', 'w'), ensure_ascii=False, indent=2)"

# メタ情報を表示
python3 -c "
import json
m = json.load(open('$MANIFEST'))
for v in m['videos']:
    if v['id'] == '$TARGET':
        print()
        print('✅ Customize プロンプトをクリップボードにコピーしました')
        print('='*70)
        print(f'🎬 動画{v[\"seq\"]:02d}｜{v[\"title\"]}')
        print(f'   対応章: {v[\"chapter\"]}')
        print(f'   Notebook 名: {v[\"notebook_name\"]}')
        print('='*70)
        print()
        print('📥 NotebookLM にアップロードする Sources:')
        for src in v['sources']:
            print(f'   - {src}')
        print()
        print('🚀 次の手順:')
        print('   1. NotebookLM で新規 Notebook を作成')
        print(f'      名前: {v[\"notebook_name\"]}')
        print('   2. 上の Sources を 2件アップロード')
        print('   3. Customize プロンプト（クリップボードにコピー済み）を貼って生成')
        print('   4. Video を生成 → ダウンロード')
        print('   5. YouTube に非公開でアップ → 埋め込みURLを取得')
        print(f'   6. bash update_video_url.sh $TARGET <YouTube_URL>')
        break"
