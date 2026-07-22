# 🎬 動画03｜自分らしさとの一致

- **LO id**: `self_alignment`
- **層**: 第1層
- **対応章**: Life is more important than business
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/self_alignment
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは「人生目的が先、事業目的は後」という順序を身体に届ける
8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「あなたの事業目標は、どこから導かれていますか？
  市場ですか、投資家ですか、それとも人生ですか」

▼ ブロック2：鏡（0:45-2:00）
  Bが「多くの経営者が、事業で成功してから人生を整えようとします。
  そして事業が成功した頃には、人生のほうが壊れています」
  【3秒沈黙】

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「For most people, life is more important than business.
  That's why your life purpose and life goal should take priority over
  your business purpose and business goal. Start with your life purpose and goals,
  then align your business ones.」
  順序を明示的に「人生 → 事業」で組み直すことが、実は最短距離である理由を、
  日常語で3つに分解。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「理想論だ。事業で稼がないと人生も成り立たない」
  Bが「その反応、"事業先行" の反射です。稼いだ後に人生を修復するコストは、
  今の30分の人生整理より高い。これは第2層 "10個のボックス" で解体します」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「事業目標が先で、人生はそれに合わせるものと思っている」。
  L4は「組織や顧客との対話で、この順序を伝え、他者の順序を整える手助けができる」。
  次の段（L2）は「大きな意思決定の前に、人生目的との整合を必ず確認する」。

▼ ブロック6：次の1手（7:00-8:00）
  「今から5分、あなたの人生目的を1文で書いてみてください。
  そしてその1文と、今週の予定の中の1つを、"揃っているか" 目で比べてください」
  【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「Design a business and life that truly aligns with who you are.
  Reflect your values and personality.」
  Bが「事業は道具です。あなたの人生に仕えます。逆ではありません」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. あなたの人生目的を1文で書けますか？書けなければ、何が邪魔していますか？
2. その1文と、今週の予定の中で最も時間を使うものは、揃っていますか？
3. ズレていたら、そのズレは "誰の期待" に応えるためのものですか？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/self_alignment）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh self_alignment <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh self_alignment

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh self_alignment <YouTube_URL>
```
