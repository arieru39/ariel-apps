#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
english-schema — SERIES 配列の同期スクリプト

単元を追加/変更する手順:
  1. english-schema/{slug}/index.html を置く（単一HTML・7スロット構成）
  2. english-schema/index.html（ハブ）の /* SERIES:BEGIN */ 〜 /* SERIES:END */ に1行足す
     ← ここが唯一の正典
  3. english-schema/field/index.html の MISSION に、その単元の任務を1行足す
  4. python3 english-schema/_series.py を実行
     → ハブの配列が全単元＋場（field）へコピーされ、台帳・ドット・配札が自動で増える

進捗キーは localStorage["ens_seen"]。slug がそのままキーになる（オリジン共有）。
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
HUB = os.path.join(HERE, "index.html")
BEGIN, END = "/* SERIES:BEGIN */", "/* SERIES:END */"

# 単元ではないが SERIES を必要とするフォルダ（場など）
EXTRA = ["field"]


def canon() -> str:
    s = open(HUB, encoding="utf-8").read()
    m = re.search(re.escape(BEGIN) + r"(.*?)" + re.escape(END), s, re.S)
    if not m:
        sys.exit("ハブに SERIES:BEGIN/END マーカーがありません")
    return m.group(1).strip()


def slugs(block: str):
    return re.findall(r'\{id:"([a-z0-9-]+)"', block)


def sync(block: str, slug: str) -> str:
    path = os.path.join(HERE, slug, "index.html")
    if not os.path.exists(path):
        return f"{slug}: MISSING index.html"
    s = open(path, encoding="utf-8").read()

    new = BEGIN + "\n" + block + "\n" + END

    # すでにマーカーがある場合は中身を差し替え
    if BEGIN in s and END in s:
        s2 = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: new, s, count=1, flags=re.S)
    else:
        # 初回: 素の const SERIES=[...]; をマーカーごと置換
        pat = re.compile(r"const SERIES=\[.*?\n\];", re.S)
        if not pat.search(s):
            return f"{slug}: SERIES 配列が見つかりません"
        s2 = pat.sub(lambda _: new, s, count=1)

    if s2 == s:
        return f"{slug}: no change"
    open(path, "w", encoding="utf-8").write(s2)
    return f"{slug}: synced"


if __name__ == "__main__":
    block = canon()
    ids = slugs(block)
    print(f"canonical units: {len(ids)} -> {', '.join(ids)}")
    for sl in ids:
        print(" ", sync(block, sl))
    for sl in EXTRA:
        print(" ", sync(block, sl), "(extra)")
