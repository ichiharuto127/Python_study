# ========================================
# 第7章: テキストファイルの読み書き
# ========================================

import os

# --- ファイルに書き込む ---
# mode="w": 新規作成 or 上書き
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Pythonの学習記録\n")
    f.write("第7章: ファイルI/O\n")

print("sample.txt を作成しました")

# --- ファイルを読み込む（全体）---
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# --- ファイルを1行ずつ読む ---
with open("sample.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.rstrip()}")   # rstrip()で末尾の改行を除去

# --- 行のリストとして読む ---
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"行数: {len(lines)}")

# --- ファイルに追記する ---
# mode="a": 追記
with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("追記しました！\n")

# --- CSVファイルの読み書き ---
# 書き込み
csv_data = [
    ["name", "goals", "assists"],
    ["田中", "20", "8"],
    ["鈴木", "15", "12"],
    ["佐藤", "10", "5"],
]

with open("players.csv", "w", encoding="utf-8") as f:
    for row in csv_data:
        f.write(",".join(row) + "\n")

# 読み込み
with open("players.csv", "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")
    print(f"ヘッダー: {header}")
    for line in f:
        values = line.strip().split(",")
        player = dict(zip(header, values))
        print(player)

# --- with文の利点 ---
# withブロックを抜けると自動的にclose()が呼ばれる
# → ファイルの閉め忘れを防げる

# --- ファイルの存在確認 ---
print(os.path.exists("sample.txt"))    # → True
print(os.path.exists("nothing.txt"))   # → False

# 後片付け
os.remove("sample.txt")
os.remove("players.csv")
print("ファイルを削除しました")
