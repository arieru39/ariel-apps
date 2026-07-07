# 📚 学習アプリ標準テンプレート（ariel-apps 系統）

このフォルダは、**ありえる楽考スタイル学習アプリ** の標準テンプレートです。
Kindle書籍1冊から、1〜2ポモドーロで新しい学習アプリを再現的に量産するための「原型」を提供します。

**参考実装**（最も完成度が高い順）:
1. 🥇 `../tamakatsu/` — フル機能（3層構造 + 各LO動画 + LO別観点クイズ + 8Q関係性クイズ + 第1層ガイド）
2. 🥈 `../talkable-school/` — 各LO観点クイズ + 第1層ガイド（動画・8Q未搭載）
3. 🥉 `../genkai/`, `../context-leadership/` — 初期テンプレ（LO別観点クイズ・動画・第1層ガイドなし）

## 🎯 標準構成（"完成形"の定義）

新しい学習アプリを作るとき、以下がすべて揃っていることを **標準** とします。

| 要素 | 必須／推奨 | 参照 |
|---|---|---|
| **3層構造** の LO 階層 | 必須 | `layers` / theme.layer |
| **各LOに動画** (`video_embed_url` + `video_title`) | 必須 | theme.video_embed_url |
| **各LOに観点クイズ** (2〜3問 × 4択、ミラー型フィードバック) | 必須 | theme.perspective_quiz |
| **8問の関係性クイズ**（テーマ横断・書籍全体の骨格を掴む） | 推奨 | relationship_quiz |
| **第1層ガイドバナー**（初めての方向け導線 + STARTバッジ） | 必須 | getting_started |
| **ルーブリック 4段階**（Fast/Slow 位相付き） | 必須 | rubric_labels |
| **エンジンノート**（Deliberate Practice 統一原理） | 必須 | engine_note |
| **書籍プレイリスト**（book-level 動画一覧） | 推奨 | book.playlist_embed_url |
| **related_apps**（他アプリの同型テーマへのリンク） | 推奨 | theme.related_apps |

## 📋 4ステップ標準ワークフロー

### Step 1. 素材の準備

- [ ] Kindle Live Text で書籍OCRを取得
- [ ] `参考図書/Kindle/<本のタイトル>/<本のタイトル>.md` に配置

### Step 2. 主張構造の抽出（Explore agent）

Explore agent に投げて以下を抽出：

- [ ] **1文で言うとこの本は何を主張しているか**
- [ ] **主要テーマ 8〜12個**（各テーマは `〜を判別できる` / `〜を選び分けられる` の形に言語化できるか）
- [ ] **3層構造**（例：土台→実装→波及 / 認知強化→熟達→価値共創 / 心→実践→品格）

**判断基準**：
- たまかつと接続できるか（貢献志向・判断軸の内部化・場のデザインとの相性）
- 学習目標として言語化できるか
- 層構造は「内→外」または「心→実践→品格」でストーリーが立つか

### Step 3. テーマ設計（data.json の中身）

各テーマに以下を割り当てる：

| 項目 | 内容 |
|---|---|
| `id` | 英語スネークケース。例: `unconscious_assumption` |
| `layer` | 1〜3。数字が大きいほど「外／統合」側 |
| `title` | 日本語1行 |
| `lo_tag` | `#英語スネークケース` |
| `seed_question` | 種の問い1行 |
| `excerpt` | OCR抜き書き100〜200字。`**強調**` 使用可 |
| `prompt` | 実務例で書かせる問い1行 |
| `rubric` | 4段階の配列（L1気づいていない → L4選び分けられる） |
| `implemented` | 本文抜き書きが埋まったら true |
| `video_embed_url` | YouTube埋め込みURL。例: `https://www.youtube.com/embed/<VIDEO_ID>` |
| `video_title` | 動画タイトル。例: `第1章 〇〇 — サブタイトル` |
| `perspective_quiz` | 動画を観る前の観点づくり（2〜3問 × 4択） |
| `related_apps` | 他アプリの同型テーマへのリンク（任意） |

### Step 4. 観点クイズの設計（各テーマ 2〜3問 × 4択）

**各問の構造**:
```json
{
  "q": "問い本文",
  "learning_objective": "この設問で掴みたいこと1行",
  "choices": [ 4つの選択肢 ]
}
```

**各選択肢の必須フィールド**:
```json
{
  "text": "選択肢テキスト",
  "stance": "🔍 視点の名前 ── スタンスのラベル",
  "phase": "⚡ Fast の反射 | 🐢 Slow の再構築 | 🌊 身体の感覚",
  "phase_note": "なぜこの位相か、1行",
  "author_view": "📖 本ではこう語られている：本文からの具体的な引用／要旨",
  "slow_question": "🌱 一段深めるための問い"
}
```

**設計原則**（Deliberate Practice の6要件）:
| 要件 | 実装 |
|---|---|
| Comprehensible Input | stance/author_view/slow_question で3層フィードバック |
| 即時のフィードバック | 選択直後に3層すべて表示 |
| 明確で具体的な目標 | 各問頭に `learning_objective`（🎯 掴みたいこと） |
| 完全な集中 | 1問1画面・判定色なし |
| コンフォートゾーンの一段外 | `slow_question` が現在地を一段だけ押し上げる |
| 専門家による設計 | `author_view` が書籍（＝専門家）の視座 |

**位相の配分の目安**（各問 4選択肢）:
- ⚡ Fast の反射: 1つ（日常の即断・脊髄反射）
- 🐢 Slow の再構築: 2つ（内省的な組み立て直し）
- 🌊 身体の感覚: 1つ（ソマティックな受信）

**author_view は必ず本文の具体箇所を引用**（抽象的な要約に逃げない）。

## 📁 配置

```
~/Workspace/ariel-apps/<slug>/
├── index.html    (この _template/index.html をそのままコピー ─ 触らない)
├── data.json    (Step 3-4 で作った中身)
└── README.md    (本の主張1文・Nテーマ・3層構造・中核ループ・公開URL)
```

## 🚀 デプロイ

```bash
cd ~/Workspace/ariel-apps
git add <slug>/ index.html
git commit -m "add <slug> learning app"
git push
```

- ランディング (`~/Workspace/ariel-apps/index.html`) に新しいアプリカードを追加
- `.app .tag.<slug>` / `.btn.<slug>` の CSS クラスを2行追加
- 公開URL: `https://arieru39.github.io/ariel-apps/<slug>/`
- 反映は通常 1〜3分。`gh run list --limit 3` で確認

## ⚠️ よくある落とし穴

- **`index.html` は触らない**。テンプレートが drift すると次回以降の量産が壊れる。改善は tamakatsu 側で先に、次に他アプリへ横展開
- **JSON構文**: `python3 -c "import json; json.load(open('data.json'))"` で必ず検証
- **JS構文**: HTMLからスクリプトを抽出して `node --check` で検証
- **GitHub Pages が transient エラー**: 空コミットで再試行 `git commit --allow-empty -m "retry deploy"`
- **localStorage 名前衝突**: `STORAGE_KEY` / `BANNER_KEY` は `applyBookMeta()` で `slug` 別に自動 namespace 化される

## 🔗 CLAUDE.md 参照

作業ログの記録・トリガーワード・出力サマリのフォーマットは **CLAUDE.md 6-9** を参照。
