# 🎬 動画10｜日々の実行リズム（Plan-Do-Reflect）

- **LO id**: `daily_execution_rhythm`
- **層**: 第3層
- **対応章**: Daily Execution Cycle
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/daily_execution_rhythm
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは「戦略は朝夜のリズムに翻訳された時にはじめて生きる」を身体に届ける
8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「あなたの組織の朝は、Plan で始まっていますか？夜は Reflect で終わっていますか？」

▼ ブロック2：鏡（0:45-2:00）
  Bが「多くの組織で、朝は "会議への駆け込み" で始まり、夜は "何となく残業" で終わります。
  だから戦略が現場に翻訳されない」
  【3秒沈黙】

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Morning: Plan. Day: Do. End of the Day: Reflect. Repeat every day.
  Not micromanagement, but rhythm and pace. This cycle establishes a steady rhythm,
  enabling consistent progress without unnecessary stress.」
  マイクロマネジメントとの違いを日常語で説明。
  リズム = 一定の呼吸、マイクロマネジメント = 常時監視。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「朝夕の10分を確保するのは、現場に負担ではないですか？」
  Bが「その反応、"忙しいから時間がない" の反射です。
  リズムの欠如が忙しさを生んでいる、という因果を試してみますか？」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「"日々の振り返り" の発想がなく、月次・四半期でしか見ていない」。
  L4は「組織全体のリズムを設計・維持し、メンバーの成長速度を上げられる」。
  次の段（L2）は「朝10分の Plan と夜10分の Reflect の意義を、現場に説明できる」。

▼ ブロック6：次の1手（7:00-8:00）
  「明日、朝10分だけ、Today's Plan（優先度3つ）を書いてください。
  そして夜10分だけ、Today's Reflect（うまくいった1つ／改善する1つ）を書いてください」
  【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「This cycle increases alignment, growth, and continuous improvement.」
  Bが「戦略はスライドではなく、朝夜のリズムに宿ります」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. 明日の朝10分 と 夜10分、あなたはどこに Plan と Reflect の時間を置きますか？
2. その10分を、忙しくても守るには、何を仕組みにしますか？
3. 2週間続けたら、あなたと現場は何を変えていますか？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/daily_execution_rhythm）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh daily_execution_rhythm <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh daily_execution_rhythm

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh daily_execution_rhythm <YouTube_URL>
```
