# 🎬 動画09｜6段階プロセスの習得

- **LO id**: `six_step_process_mastery`
- **層**: 第3層
- **対応章**: Simple Strategy Process
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/six_step_process_mastery
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは第3層の入口。「戦略は一度立てたら終わりではなく、6段階のループを回すもの」
を身体に届ける 8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「あなたの組織の戦略は、"一度立てて実行" ですか、それとも "回し続ける" ですか？」

▼ ブロック2：鏡（0:45-2:00）
  Bが「多くの組織が、年度計画を立てて12ヶ月実行するだけ、というリズムで回っています。
  でも本書の6段階は、"回す" ことでしか身につかない」
  【3秒沈黙】

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Simple Strategy Process — Six essential steps: Purpose and Goal,
  Opportunity Finding, Strategic Core, Action Plan, Execution and Results,
  Review and Refinement. Review, refine, and repeat.」
  6段階を一度だけ順に紹介し、"Review & Refinement" から次の Purpose に戻る循環が
  組織の学習曲線を作る、と説明。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「6段階も回してたら、意思決定が遅くなる」
  Bが「その反応、"素早く決めきる = 良い" の反射です。実は6段階を高速に回す方が、
  1段階を長く滞留させるより速い。これは次のLO『10個のボックス』で解体します」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「"戦略を立てる" とは1度のイベントだと思っている」。
  L4は「6段階を組織の呼吸にし、成長段階ごとにループの速度を選び直せる」。
  次の段（L2）は「6段階のうち、あなたの組織で最も飛ばされている段階を指せる」。

▼ ブロック6：次の1手（7:00-8:00）
  「今から3分、6段階（Purpose / Opportunity / Strategic Core / Action Plan / Execution / Review）
  のうち、あなたの組織で最も飛ばされている段階を1つ選んでください」【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「Review, refine, and repeat — this loop makes strategy evolve.」
  Bが「ループを回す組織は、賢くなる組織です」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. 6段階のうち、あなたの組織で最も飛ばされているのはどこですか？
2. Review & Refinement から次の Purpose に戻る場は、どこにありますか？
3. その飛ばされた段階を来週、どこにどれくらい入れますか？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/six_step_process_mastery）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh six_step_process_mastery <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh six_step_process_mastery

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh six_step_process_mastery <YouTube_URL>
```
