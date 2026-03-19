# ========================================
# 第4章: strクラスのメソッド
# ========================================

from cmath import e
from tkinter import E


s = "  Hello, Python World!  "

# --- 空白の除去 ---
es = s.strip()
ls = s.lstrip()
rs = s.rstrip()
print(es)       # → "Hello, Python World!"（両端）
print(ls)      # → "Hello, Python World!  "（左のみ）
print(rs)      # → "  Hello, Python World!"（右のみ）

# --- 大文字・小文字 ---
print(es.upper())       # → "HELLO, PYTHON WORLD!" (すべて大文字)
print(es.lower())       # → "hello, python world!" (すべて小文字)
print(es.capitalize())  # → "Hello, python world!"（先頭のみ大文字）
print(es.title())       # → "Hello, Python World!"（各単語の先頭大文字）

# --- 検索・置換 ---
text = "Python is great. Python is fun."
print(text.find("Python"))     # → 0   （最初の位置）
print(text.count("Python"))    # → 2   （出現回数）
print(text.replace("Python", "Java"))
# → Java is great. Java is fun.　("Python"をすべて"Java"に置換)

# --- 分割・結合 ---
csv_line = "田中,85,A"
parts = csv_line.split(",")    # 文字列を,で分割してリストで返す
print(parts)           # → ['田中', '85', 'A']

words = ["Python", "is", "fun"]
print(" ".join(words)) # → Python is fun
print("-".join(words)) # → Python-is-fun

# --- 判定系 ---
print("12345".isdigit())    # → True   数字のみ
print("hello".isalpha())    # → True   アルファベットのみ
print("hello123".isalnum()) # → True   英数字のみ
print("  ".isspace())       # → True   空白のみ
print("Hello".startswith("He"))  # → True  先頭がHeかどうか
print("Hello".endswith("lo"))    # → True  末尾がloかどうか

# --- formatメソッド ---
name = "太郎"
score = 92.5
print("{0}の点数は{1:.1f}点です".format(name, score))
# → 太郎の点数は92.5点です

# f文字列
print(f"{name}の点数は{score:.1f}点です")

# --- ゼロ埋め・幅指定 ---
print(f"{'No.' + str(1):>10}")      # 右寄せ10文字
print(f"{42:05d}")                  # → 00042 ゼロ埋め5桁
print(f"{3.14159:.3f}")             # → 3.142 小数点3桁
print(f"{1000000:,}円")             # → 1,000,000円 カンマで3桁ごとに区切る