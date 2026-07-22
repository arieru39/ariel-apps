# 🎬 動画06｜差別化軸（便益 × 独自性）

- **LO id**: `differentiation_frame`
- **層**: 第2層
- **対応章**: Differentiation
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/differentiation_frame
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは「独自性 ≠ 差別化」を解体する 8〜10分の対話式動画です。
差別化 = 高い便益 × 高い独自性 の掛け算。

▼ ブロック1：フック（0:00-0:45）
  Aが「"あなたの独自性を1つ挙げてください" と聞かれて、
  その独自性は "顧客の生活" と繋がっていますか？」

▼ ブロック2：鏡（0:45-2:00）
  Bが「珍しいから、というだけの独自性は、顧客の目にも社員の目にも映りません。
  なぜなら、便益に繋がっていないから」
  【3秒沈黙】

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Differentiation = High Benefit × High Uniqueness.
  Benefit — The tangible improvement your product provides to customers' lives.
  Uniqueness — The value only you can provide.
  Uniqueness is not just about being different; it should reflect 'your own identity!'」
  掛け算の4象限（高便益・低独自性／低便益・高独自性／低便益・低独自性／高便益・高独自性）
  を1回だけ整理して見せる。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「価格が競合より安い、が独自性ではダメですか？」
  Bが「"安さ" は誰でも真似できます。明日、競合が同じ価格になったら、
  あなたの独自性は何が残りますか？」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「差別化を "他社との違い" とだけ捉え、便益との掛け算になっていない」。
  L4は「市場の変化に応じて、独自性と便益の掛け算を選び直せる」。
  次の段（L2）は「あなたのビジネスの便益と独自性を、1文ずつ言える」。

▼ ブロック6：次の1手（7:00-8:00）
  「今から3分、あなたのビジネスの "便益" と "独自性" を、それぞれ1行で書いて、
  その2つが掛け算になっているか、目で確かめてください」【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「Your uniqueness should reflect 'your own identity!'
  and provide clear benefit to your target customers.」
  Bが「独自性は、あなたが誰であるかから湧き出るもの。真似できないのは、そこだけです」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. あなたのビジネスの便益と独自性を、それぞれ1行で書いてください
2. その2つは、掛け算になっていますか？どちらが弱いですか？
3. 明日、競合が同価格・同機能で来たら、あなたに何が残りますか？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/differentiation_frame）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh differentiation_frame <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh differentiation_frame

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh differentiation_frame <YouTube_URL>
```
