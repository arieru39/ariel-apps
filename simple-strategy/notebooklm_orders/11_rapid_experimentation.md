# 🎬 動画11｜素早い試行（10個のボックス）

- **LO id**: `rapid_experimentation`
- **層**: 第3層
- **対応章**: Theory of Ten Boxes
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/rapid_experimentation
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは第3層の閉じ。「失敗を実験と呼び直し、試行の速度と数を上げる」
を身体に届ける 8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「あなたが今、"やってみたいけど失敗が怖い" と思っているアイデアはいくつありますか？」

▼ ブロック2：鏡（0:45-2:00）
  Bが「10個のボックスの前にあなたが立っています。中身は見えません。
  1つに宝が入っている。あなたはどう動きますか？」
  【3秒沈黙】「1つに絞って全力、が多くの組織の反射です。でも数式は言います」

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Ten Boxes: Only one contains treasure. You cannot see inside from outside.
  To win, you need to open the boxes as quickly as possible.
  Success Formula: Successes = Attempts × Success Rate.
  Prioritize rapid iteration over perfection.」
  試行数 × 成功率 の数式が、"選択と集中" の反射をどう解体するか、
  ボーイングの新型機開発のケースで見せる。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「試行を増やすと、コストが積み上がる」
  Bが「そのコストは、1つに絞って外れた時の "戻れないコスト" と比べていますか？」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「失敗を恥と考え、試行数を増やす発想がない」。
  L4は「組織文化として "実験の速度" が定着し、確率的思考で経営できる」。
  次の段（L2）は「失敗を "実験" と呼び直したら、社内の空気がどう変わるか、想像できる」。

▼ ブロック6：次の1手（7:00-8:00）
  「今から3分、あなたが "失敗が怖くて動けない" 案を3つ書いてください。
  そして、その3つを "実験" と呼び直して、
  それぞれ 3週間以内に検証できる最小の一歩 を書いてください」【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「Prioritize rapid iteration over perfection.
  Each box represents a new business. Successes = Attempts × Success Rate.」
  Bが「実験は失敗しません。実験は "情報を返す" だけです」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. あなたが "失敗が怖くて動けない" 案を3つ挙げてください
2. その3つを "実験" と呼び直したら、それぞれ3週間以内に検証できる最小の一歩は？
3. 組織で "失敗" を "実験" と呼び直す文化を、あなたはどう仕込みますか？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/rapid_experimentation）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh rapid_experimentation <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh rapid_experimentation

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh rapid_experimentation <YouTube_URL>
```
