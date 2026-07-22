# 🎬 動画07｜事業サイクル（Create/Make/Sell）

- **LO id**: `business_cycle_rhythm`
- **層**: 第2層
- **対応章**: Basic Business Cycle
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/business_cycle_rhythm
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは「Create → Make → Sell → Feedback → Create の循環が
組織の呼吸である」を身体に届ける 8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「今週、顧客からのフィードバックが、あなたの次の Create にどう戻っていますか？」

▼ ブロック2：鏡（0:45-2:00）
  Bが「多くの組織で、フィードバックは "褒め言葉" として消費され、
  次の Create の入力にはなっていません。だからサイクルが止まる」
  【3秒沈黙】

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Once you sell, you reach customers. Their response and requests come back
  as feedback or customer insights. These insights help improve Create, Make, and Sell,
  enabling your business to evolve. The faster and smoother this cycle spins,
  the stronger your business becomes.」
  Create / Make / Sell のどれか1つが詰まると、全体の速度が落ちる理由を、
  自転車のギアで例える。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「フィードバックは大切だと分かってるけど、忙しくて拾えない」
  Bが「その "忙しい" の中身が、循環が止まっている症状です。
  拾えないのではなく、拾う仕組みがないだけ」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「Create/Make/Sell が分断的にしか見えない」。
  L4は「組織の呼吸として3ステップが循環し、事業の進化速度を体感できる」。
  次の段（L2）は「今週のフィードバックを、次の Create に翻訳する場を持てる」。

▼ ブロック6：次の1手（7:00-8:00）
  「今週の顧客からのフィードバックを1つ思い出してください。
  それを、次の Create のどこに反映するか、1文で書いてください」【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「The faster and smoother this cycle spins, the stronger your business becomes.」
  Bが「循環の速度は、才能ではなく、設計です」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. あなたのビジネスの Create/Make/Sell のうち、最も詰まっているのはどこですか？
2. 顧客からのフィードバックは、"次の Create" にどう戻っていますか？
3. 循環を復活させるために、あなたが今週始められる小さな一手は？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/business_cycle_rhythm）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh business_cycle_rhythm <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh business_cycle_rhythm

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh business_cycle_rhythm <YouTube_URL>
```
