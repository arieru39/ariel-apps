# 🎬 動画05｜機会と適性の交差点（Three Circles）

- **LO id**: `opportunity_mapping`
- **層**: 第2層
- **対応章**: Opportunity Finding
- **推奨尺**: 8〜10分（対話式2名）

---

## 📥 Sources（NotebookLM にアップロードする）

1. **OCR**: `/Users/suzukitoshikazux/ありえるObsidian/35参考図書/Kindle/Kindle文字起こし/simple strategy/simple strategy.md`
2. **data.json**: `/Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/data.json`

**Notebook 名（NotebookLM で作成時）**：
```
ariel-apps/simple-strategy/opportunity_mapping
```

---

## 🎯 Customize プロンプト（下のブロックを Customize に貼る）

```
このLOは「情熱・スキル・市場需要の3円が交差するスイートスポットにだけ、
続けられる事業がある」を身体に届ける 8〜10分の対話式動画です。

▼ ブロック1：フック（0:00-0:45）
  Aが「あなたが情熱を持てて、得意で、市場が欲しがっている ── 
  この3つが重なった瞬間を、最後にいつ経験しましたか？」

▼ ブロック2：鏡（0:45-2:00）
  Bが「情熱だけで始めた事業は疲弊します。
  スキルだけで始めた事業は退屈します。
  市場だけで始めた事業は、あなたが消えます」
  【3秒沈黙】

▼ ブロック3：原理の解剖（2:00-4:00）
  原典引用：「Find the sweet spot where the three elements overlap:
  What you want to provide, What you are good at, What your customers want.
  Don't ignore any circle. Customer needs are crucial — even if you're passionate
  and skilled, there must be real demand.」
  3円のどれか1つを空欄にすると、事業がどう歪むかを、3ケースで見せる。

▼ ブロック4：Fast の反射（4:00-5:30）
  Aが「一番情熱を持てる案を選べば、あとは何とかなる」
  Bが「"好きこそ物の上手なれ" の反射です。情熱だけで顧客ゼロだった過去の事業は、
  なぜ止まったか、思い出せますか？」

▼ ブロック5：次の段の景色（5:30-7:00）
  L1→L4：L1は「情熱だけで事業を始め、市場需要の検証をしない」。
  L4は「3円の重なりの動きを察知し、機会を逃さず選び直せる」。
  次の段（L2）は「3円のどれが今、最も検証が甘いか、身体で指せる」。

▼ ブロック6：次の1手（7:00-8:00）
  「今から3分、あなたの現在の事業で、3円のうち "検証が最も甘い円" を1つ選び、
  今週それをどう検証するか、1行で書いてください」【動画を止めてください】

▼ ブロック7：閉じ（8:00-8:30）
  原典引用：「Customer needs are crucial — even passion and skill are not enough
  without real demand.」
  Bが「3円の交差点は、机の上ではなく、現場でしか見つかりません」
```

---

## 🌱 深掘り問い（動画視聴後、アプリ内で回答用）

1. 今、あなたの事業で最も検証が甘い円は、情熱／スキル／市場需要のどれですか？
2. その円を今週、どの現場で確かめる予定ですか？
3. 3円の重なりを1文で表現するとしたら？


---

## ✅ この動画の完了チェック

- [ ] Notebook を作成した（ariel-apps/simple-strategy/opportunity_mapping）
- [ ] Sources を 2件アップした（OCR + data.json）
- [ ] 上の Customize プロンプトを貼って生成した
- [ ] MP4/MP3 をダウンロードした
- [ ] YouTube に非公開でアップした
- [ ] YouTube 埋め込みURLを取得した（`https://www.youtube.com/embed/<VIDEO_ID>` 形式）
- [ ] `bash update_video_url.sh opportunity_mapping <YouTube埋め込みURL>` を実行した
- [ ] `data.json` の `video_embed_url` が更新されたことを確認した

---

## 🚀 次のアクション

```bash
# このプロンプトをクリップボードにコピー
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/paste_prompt.sh opportunity_mapping

# 生成完了後、YouTube URLをアプリに反映
bash /Users/suzukitoshikazux/Workspace/ariel-apps/simple-strategy/notebooklm_orders/update_video_url.sh opportunity_mapping <YouTube_URL>
```
