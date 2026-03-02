# ========================================
# 第3章: whileループ
# ========================================

# --- 基本のwhile文 ---
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
# → 0 1 2 3 4
print()

# --- breakで脱出 ---
n = 0
while True:          # 無限ループ
    n += 1
    if n >= 5:
        break        # 条件を満たしたら脱出
print(f"n = {n}")   # → n = 5

# --- whileとcontinue ---
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue     # 3の倍数はスキップ
    print(i, end=" ")
# → 1 2 4 5 7 8 10
print()

# --- カウントダウンタイマー ---
count = 5
while count > 0:
    print(f"あと{count}秒...")
    count -= 1
print("スタート！")

# --- 実践例: 正の数が入力されるまで繰り返す ---
while True:
    value = int(input("正の整数を入力してください: "))
    if value > 0:
        print(f"{value}の二乗は{value**2}です")
        break
    else:
        print("正の整数を入力してください！")

# --- while vs for の使い分け ---
# for  → 繰り返す回数が決まっているとき
# while → 条件が満たされるまで繰り返すとき

# 例: コラッツ予想（1になるまで繰り返す）
n = 27
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1
print(f"27から1になるまで{steps}ステップ")  # → 111ステップ
