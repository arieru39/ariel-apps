# 🎬 動画02｜穏やかな心

- **LO id**: `calm_mindset`
- **層**: 第1層
- **対応章**: Strategy is a direction
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/calm_mindset
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは「戦略は勝ち負けではなく、穏やかで興奮できる方向である」
と気づかせる 8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「"戦略" と聞いた瞬間、あなたの身体が最初に感じるのは何ですか？」
  Bが「緊張ですか、興奮ですか。答えが緊張なら、
  今日の30分は "戦略" の意味を書き換える時間です」

▼ ブロック2：鏡（0:45-2:00）
  Bが「戦略の本の多くが、勝ち負け・競争・戦いのメタファーで語られます。
  でもそのメタファーで疲れているのは、あなただけではありません」
  【3秒沈黙】「勝ち続けている経営者ほど、実は穏やかです」

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Strategy is often associated with winning, losing, competition, and battle.
  This book takes a different view. I see strategy as a direction and a set of actions
  to achieve your purpose and goal. What matters is staying relaxed and excited about what you do.」
  「穏やかさ」と「興奮」は矛盾ではない。緊張の反対は倦怠、穏やかさの反対は焦り。
  この4象限を1回だけ整理して見せる。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「でも緩んでいたら競合に負ける」
  Bが「その反応、"戦略 = 戦い" の反射です。競合との勝ち負けは、あなたの人生目的の
  何番目ですか？次の第1層LO『自分らしさとの一致』で解体します」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「戦略は "勝ち負け" のフレームで、常に緊張と警戒が伴う」。
  L4は「組織全体の空気を "穏やかな興奮" にファシリテートできる」。
  次の段（L2）は「大事な意思決定の直前、意識して穏やかな状態に自分を戻せる」。

▼ ブロック6：次の1手（7:00-8:00）
  「明日、あなたが最も緊張する会議の前に、3分だけ深呼吸をしてください。
  そして "今日の目的は勝つことではなく、方向を確かめること" と1回だけ言ってください」
  【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「Creating and executing strategy doesn't require you to be cold, tense,
  or overly afraid of failure.」
  Bが「穏やかな戦略は、遅い戦略ではありません。むしろ、続く戦略です」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. あなたが "戦略" と聞いた時に身体に走るのは、緊張／興奮／諦め／穏やかさ、どれですか？
2. 過去、あなたが最も穏やかで最も成果が出た時期を、1つ思い出せますか？
3. その時期の "穏やかさの源" は、環境ですか、心構えですか、両方ですか？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/calm_mindset）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh calm_mindset <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh calm_mindset

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh calm_mindset <YouTube_URL>
```
