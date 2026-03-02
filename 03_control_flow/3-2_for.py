# ========================================
# 第3章: forループ・rangeオブジェクト
# ========================================

# --- リストのfor文 ---
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# → apple
# → banana
# → cherry

# --- rangeオブジェクト ---
# range(stop)        : 0 〜 stop-1
# range(start, stop) : start 〜 stop-1
# range(start, stop, step) : stepずつ増加

for i in range(5):
    print(i, end=" ")   # → 0 1 2 3 4
print()

for i in range(1, 6):
    print(i, end=" ")   # → 1 2 3 4 5
print()

for i in range(0, 10, 2):
    print(i, end=" ")   # → 0 2 4 6 8
print()

# 逆順
for i in range(5, 0, -1):
    print(i, end=" ")   # → 5 4 3 2 1
print()

# --- enumerate: インデックスと値を同時に取得 ---
members = ["田中", "鈴木", "佐藤"]
for i, name in enumerate(members):
    print(f"{i+1}番: {name}")
# → 1番: 田中
# → 2番: 鈴木
# → 3番: 佐藤

# --- breakとcontinue ---
# break: ループを終了
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")   # → 0 1 2 3 4
print()

# continue: 以降をスキップして次のループへ
for i in range(10):
    if i % 2 == 0:
        continue        # 偶数はスキップ
    print(i, end=" ")   # → 1 3 5 7 9
print()

# --- ネストしたforループ ---
for i in range(1, 9):
    for j in range(1, 9):
        print(f"{i}×{j}={i*j}", end=" ")
    print()
# → 九九の表

# --- リスト内包表記（シンプルなforループの省略形）---
squares = [x**2 for x in range(1, 6)]
print(squares)   # → [1, 4, 9, 16, 25]

evens = [x for x in range(20) if x % 2 == 0]
print(evens)     # → [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# --- 実践例: 合計・平均を求める ---
scores = [78, 92, 65, 88, 71, 95, 83]
total = 0
for s in scores:
    total += s
average = total / len(scores)
print(f"合計: {total}, 平均: {average:.1f}")
