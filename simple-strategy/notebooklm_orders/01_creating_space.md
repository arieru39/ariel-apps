# 🎬 動画01｜空間をつくる

- **LO id**: `creating_space`
- **層**: 第1層
- **対応章**: Create Space
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/creating_space
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは「戦略思考の起点は、机の上でも頭の中でも "空間をつくる" こと」
という気づきに聞き手を運ぶ 8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「今、机の上に書類が何冊積まれていますか？受信箱に未読は何通ありますか？」
  Bが「その物量そのものが、あなたの新しい戦略を潰しています」

▼ ブロック2：鏡（0:45-2:00）
  Bが「戦略の会議の朝、あなたが最初にすることは、議題を埋めることですか？
  それとも、机と頭を空けることですか？」
  【3秒沈黙】

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Create space. Clear your desk, tidy your inbox, and let go of low-priority projects.
  Above all, clear your mind of worries and distractions.」
  空間は "物理・デジタル・時間・心" の4領域。どれか1つでも詰まると、他の3つに漏れ出す。
  Bが「思考の余白は、机の余白と繋がっています」

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「でも、机を空けたら仕事が進んでる感じがしなくて、不安になる」
  Bが「その不安、まさに Fast の反射です。"忙しくしていないと安心できない" という
  無意識の思い込みが動いている音。今はまだ手放さなくていい。ただ "音がした" と気づくだけ」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「"空間をつくる" という発想がなく、忙しさを埋めることが仕事だと思っている」。
  L4は「大事な意思決定の前に、自動で空間をつくり、周囲にもそれを促せる」。
  次の段（L2）は「今週、物理・デジタル・時間・心の4領域のどれが最も詰まっているか、
  身体で1つ指せる」。

▼ ブロック6：次の1手（7:00-8:00）
  「今から3分だけ、机の上のものを3つ、視界の外に移してください。
  それから受信箱の未読を3通、アーカイブしてください」【動画を止めてください】
  「変わらなくても大丈夫。それが明日の入口です」

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「When you create space, you will gain mental clarity, know what to focus on,
  and have more capacity to generate ideas and think about new strategies.」
  Bが「空間は贅沢ではありません。戦略の必需品です」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. 今、物理・デジタル・時間・心の4領域のうち、最も詰まっているのはどれですか？
2. 空間をつくった直後に訪れるのは、"焦点の問い" ですか、それとも "詰め込みの誘惑" ですか？
3. 明日の朝、5分だけ "空白" を守るとしたら、それはどの5分ですか？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/creating_space）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh creating_space <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh creating_space

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh creating_space <YouTube_URL>
```
