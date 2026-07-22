#!/usr/bin/env python3
"""
Simple Strategy 用の NotebookLM 発注書を、
プロンプト_学習アプリのLO動画をNotebookLMでつくる_SimpleStrategy.md
から抽出して、12個のマークダウンファイルに分解する。

生成物：
  00_meta_全体像.md
  01_creating_space.md
  02_calm_mindset.md
  ...
  11_rapid_experimentation.md
  manifest.json
  state.json
"""
import re
import json
import os
from pathlib import Path

# 入力
SRC = Path("/Users/suzukitoshikazux/ありえるObsidian/07プロンプト/プロンプト/プロンプト_学習アプリのLO動画をNotebookLMでつくる_SimpleStrategy.md")
# 出力先
DST_DIR = Path(__file__).parent

# 動画メタデータ（順序と slug の対応）
VIDEOS = [
    {"seq": 0,  "id": "meta",                    "layer": None, "title": "全体像のルーブリックと11のLO", "chapter": "Introduction＋全編"},
    {"seq": 1,  "id": "creating_space",          "layer": 1,    "title": "空間をつくる", "chapter": "Create Space"},
    {"seq": 2,  "id": "calm_mindset",            "layer": 1,    "title": "穏やかな心", "chapter": "Strategy is a direction"},
    {"seq": 3,  "id": "self_alignment",          "layer": 1,    "title": "自分らしさとの一致", "chapter": "Life is more important than business"},
    {"seq": 4,  "id": "strategic_core_focus",    "layer": 2,    "title": "戦略的焦点（Who/What/How）", "chapter": "Strategic Core"},
    {"seq": 5,  "id": "opportunity_mapping",     "layer": 2,    "title": "機会と適性の交差点（Three Circles）", "chapter": "Opportunity Finding"},
    {"seq": 6,  "id": "differentiation_frame",   "layer": 2,    "title": "差別化軸（便益 × 独自性）", "chapter": "Differentiation"},
    {"seq": 7,  "id": "business_cycle_rhythm",   "layer": 2,    "title": "事業サイクル（Create/Make/Sell）", "chapter": "Basic Business Cycle"},
    {"seq": 8,  "id": "action_plan_elements",    "layer": 2,    "title": "行動計画の6要素", "chapter": "Six Elements for Action Planning"},
    {"seq": 9,  "id": "six_step_process_mastery","layer": 3,    "title": "6段階プロセスの習得", "chapter": "Simple Strategy Process"},
    {"seq": 10, "id": "daily_execution_rhythm",  "layer": 3,    "title": "日々の実行リズム（Plan-Do-Reflect）", "chapter": "Daily Execution Cycle"},
    {"seq": 11, "id": "rapid_experimentation",   "layer": 3,    "title": "素早い試行（10個のボックス）", "chapter": "Theory of Ten Boxes"},
]

# 共通 Sources
OCR_PATH = "/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md"
DATA_JSON = "/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json"

def extract_section(src_text, header_marker, next_header_marker):
    """指定されたヘッダマーカーから次のヘッダマーカーまでを抽出"""
    start = src_text.find(header_marker)
    if start == -1:
        return None
    end = src_text.find(next_header_marker, start + len(header_marker))
    if end == -1:
        return src_text[start:]
    return src_text[start:end]

def extract_customize_block(section_text):
    """```で囲まれたCustomizeプロンプト本体だけを抽出"""
    m = re.search(r"🎯 カスタマイズプロンプト.*?\n```\n(.*?)\n```", section_text, re.DOTALL)
    if not m:
        return None
    return m.group(1).strip()

def extract_deep_questions(section_text):
    """深掘り問い（🌱 深掘り問い〜 の後の番号付きリスト）を抽出"""
    m = re.search(r"🌱 深掘り問い.*?\n(.*?)(?=\n---|\Z)", section_text, re.DOTALL)
    if not m:
        return []
    lines = m.group(1).strip().splitlines()
    questions = []
    for line in lines:
        m2 = re.match(r"^\d+\.\s+(.+)$", line.strip())
        if m2:
            questions.append(m2.group(1).strip())
    return questions

def main():
    src_text = SRC.read_text(encoding="utf-8")

    manifest = {"videos": []}

    # セクションのヘッダマーカーを生成
    section_markers = []
    for v in VIDEOS:
        if v["id"] == "meta":
            section_markers.append("## 🎬 動画0：メタ動画")
        else:
            section_markers.append(f"## 🎬 動画{v['seq']}：LO{v['seq']}")
    section_markers.append("## 📊 LO一覧表")  # 終端

    for i, video in enumerate(VIDEOS):
        section = extract_section(src_text, section_markers[i], section_markers[i+1])
        if not section:
            print(f"⚠️  Section not found for video {video['seq']} ({video['id']})")
            continue

        customize = extract_customize_block(section)
        deep_qs = extract_deep_questions(section)

        # 出力ファイル
        if video["id"] == "meta":
            fname = "00_meta_全体像.md"
        else:
            fname = f"{video['seq']:02d}_{video['id']}.md"

        # Sources を組み立てる
        sources = [
            f"1. **OCR**: `{OCR_PATH}`",
            f"2. **data.json**: `{DATA_JSON}`",
        ]

        # ファイル内容
        title = video["title"]
        layer_label = f"第{video['layer']}層" if video["layer"] else "メタ（全体像）"
        chapter = video["chapter"]

        content = f"""# 🎬 動画{video['seq']:02d}｜{title}

- **LO id**: `{video['id']}`
- **層**: {layer_label}
- **対応章**: {chapter}
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

{chr(10).join(sources)}

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/{video['id']}
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
{customize}
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

"""
        for j, q in enumerate(deep_qs, 1):
            content += f"{j}. {q}\n"

        content += f"""

---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/{video['id']}）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh {video['id']} <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh {video['id']}

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh {video['id']} <YouTube_URL>
```
"""

        out_path = DST_DIR / fname
        out_path.write_text(content, encoding="utf-8")
        print(f"✅ {fname}")

        manifest["videos"].append({
            "seq": video["seq"],
            "id": video["id"],
            "layer": video["layer"],
            "title": title,
            "chapter": chapter,
            "file": fname,
            "customize_prompt": customize,
            "deep_questions": deep_qs,
            "sources": [OCR_PATH, DATA_JSON],
            "notebook_name": f"ariel-apps/simple-strategy/{video['id']}",
        })

    # manifest.json 保存
    (DST_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"\n✅ manifest.json ({len(manifest['videos'])} videos)")

    # state.json 初期化（既存の場合は上書きしない）
    state_path = DST_DIR / "state.json"
    if not state_path.exists():
        state = {v["id"]: {"status": "pending", "video_url": None, "generated_at": None} for v in VIDEOS}
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✅ state.json initialized")
    else:
        print(f"ℹ️  state.json exists, keeping current progress")

if __name__ == "__main__":
    main()
