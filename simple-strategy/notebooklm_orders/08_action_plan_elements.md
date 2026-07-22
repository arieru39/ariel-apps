# 🎬 動画08｜行動計画の6要素

- **LO id**: `action_plan_elements`
- **層**: 第2層
- **対応章**: Six Elements for Action Planning
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/action_plan_elements
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは「タスク・目的・優先度・所有者・期限・成果の6要素で
戦略が現場に翻訳される」を身体に届ける 8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「あなたのタスクリストで、"なぜやるのか（目的）" が書かれているものは、
  何％ですか？」

▼ ブロック2：鏡（0:45-2:00）
  Bが「タスクリストの多くが "やることだけ" のリストです。
  目的・所有者・期限・成果が抜けていると、そのタスクは動きません」
  【3秒沈黙】

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Six Elements for Action Planning: Task, Purpose, Priority, Owner,
  Deadline, Output. Break It Down to Speed It Up. Decide Together — actions
  should be determined through dialogue.」
  6要素のうち、日本の組織で最も抜けやすい "Purpose" と "Owner" を強調。
  「みんなの仕事は誰の仕事でもない」の解体。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「所有者を1人に決めると、責任が偏るのが心配」
  Bが「その反応、"責任分散" の反射です。所有者不在は、責任の分散ではなく、
  誰も動けない状態を作ります」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「"やることリスト" 止まりで、目的・所有者・期限が抜けている」。
  L4は「6要素を組織文化として定着させ、他者のタスク設計を整えられる」。
  次の段（L2）は「今のタスクリストから1つ選び、6要素すべてを書き出せる」。

▼ ブロック6：次の1手（7:00-8:00）
  「今から3分、あなたのタスクリストから1つ選び、
  タスク・目的・優先度・所有者・期限・成果 の6要素すべてを書き出してください」
  【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「Decide Together — actions should be determined through dialogue.」
  Bが「6要素を対話で決めた瞬間、そのタスクは "誰かの仕事" ではなく "私たちの仕事" になります」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. 今のタスクリストの中で、6要素すべてが書かれているタスクは何％ですか？
2. 最も抜けやすい要素は、目的／所有者／成果／期限、どれですか？
3. 所有者を1人に明示的に決めた時、そのタスクはどう変わりますか？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/action_plan_elements）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh action_plan_elements <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh action_plan_elements

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh action_plan_elements <YouTube_URL>
```
