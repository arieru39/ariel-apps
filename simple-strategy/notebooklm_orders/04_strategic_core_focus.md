# 🎬 動画04｜戦略的焦点（Who/What/How）

- **LO id**: `strategic_core_focus`
- **層**: 第2層
- **対応章**: Strategic Core
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/strategic_core_focus
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは「幅広く狙うのが正義」というウソを解体し、
「焦点は削ぐことで生まれる」を身体に届ける 8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「"あなたのターゲット顧客は誰ですか？" と聞かれて、
  何秒で1人の名前が浮かびますか？」

▼ ブロック2：鏡（0:45-2:00）
  Bが「"幅広く狙う" と答えた瞬間、あなたのビジネスは、
  誰にも "これは私のためのものだ" と感じてもらえなくなります」
  【3秒沈黙】

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Focus on 'who' — Choose a well-defined target customer.
  By narrowing your focus on your target customer, you can create a product or service
  that makes your customer feel, 'This is made for me.'
  A product that tries to serve everyone ends up being average for all.」
  Who → What → How の順に、各軸を "1文で言い切れるか" のテスト。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「絞ると機会を失うでしょ」
  Bが「その反応こそが "焦点の欠落" を作っている根っこです。
  幅広く狙って、これは私のためだと感じてくれた顧客は、何人いましたか？」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「幅広く狙うことが正義だと思い、焦点を絞れない」。
  L4は「Who/What/How の整合を、事業の成長段階に応じて選び直せる」。
  次の段（L2）は「Whoを1人に絞ったら、What/Howがどう変わるか、想像できる」。

▼ ブロック6：次の1手（7:00-8:00）
  「今から3分、あなたのビジネスの Who を、名前が浮かぶくらい具体的な1人の顧客像で
  書いてください。年齢・業界・課題まで」【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「Make your customer feel, 'This is made for me.'」
  Bが「1人に深く届いた瞬間、その1人の後ろには同じ悩みを持つ100人がいます」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. あなたの Who を、名前が浮かぶくらい具体的な1人で書いてください
2. その1人が満足したとき、その周りに何人の同じ悩みを持つ人がいますか？
3. 経営陣3人に Who/What/How を尋ねたら、答えは揃いますか？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/strategic_core_focus）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh strategic_core_focus <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh strategic_core_focus

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh strategic_core_focus <YouTube_URL>
```
