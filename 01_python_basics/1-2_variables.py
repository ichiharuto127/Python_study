# ========================================
# 第1章: 変数の基本
# ========================================

# 変数への代入
name = "田中"
age = 20
height = 175.5
is_student = True

print(name)        # → 田中
print(age)         # → 20
print(height)      # → 175.5
print(is_student)  # → True

# 変数を使った計算
x = 10
y = 3
print(x + y)   # → 13
print(x * y)   # → 30
print(x ** y)  # → 1000

# 変数の値の更新
score = 80
score = score + 10  # 同じ変数に再代入
print(score)        # → 90

# 省略形（複合代入演算子）
score += 5   # score = score + 5
print(score) # → 95

# 複数の変数への同時代入
a, b, c = 1, 2, 3
print(a, b, c)  # → 1 2 3

# 変数の型を確認
print(type(name))       # → <class 'str'>
print(type(age))        # → <class 'int'>
print(type(height))     # → <class 'float'>
print(type(is_student)) # → <class 'bool'>

# 文字列と変数を組み合わせた出力
print(f"{name}さんは{age}歳、身長{height}cmです")
