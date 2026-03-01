# ========================================
# 第2章: 文字列・リスト操作
# ========================================

# ===== 文字列 =====

text = "Hello, Python!"

# 長さ
print(len(text))         # → 14

# インデックスアクセス（0始まり）
print(text[0])           # → H
print(text[-1])          # → !  (末尾から)

# スライス [start:end]（endは含まない）
print(text[0:5])         # → Hello
print(text[7:])          # → Python!
print(text[:5])          # → Hello

# 文字列の結合と繰り返し
print("Hello" + " " + "World")  # → Hello World
print("Ha" * 3)                  # → HaHaHa

# f文字列（変数の埋め込み）
name = "太郎"
score = 95
print(f"{name}の点数: {score}点")       # → 太郎の点数: 95点
print(f"小数点2桁: {3.14159:.2f}")      # → 小数点2桁: 3.14

# in演算子（含まれるか確認）
print("Python" in text)   # → True
print("Java" in text)     # → False

# ===== リスト =====

fruits = ["apple", "banana", "cherry"]

# インデックスアクセス
print(fruits[0])    # → apple
print(fruits[-1])   # → cherry

# スライス
print(fruits[0:2])  # → ['apple', 'banana']

# 長さ
print(len(fruits))  # → 3

# 要素の変更
fruits[1] = "mango"
print(fruits)       # → ['apple', 'mango', 'cherry']

# 要素の追加
fruits.append("grape")
print(fruits)       # → ['apple', 'mango', 'cherry', 'grape']

# in演算子
print("apple" in fruits)   # → True
print("orange" in fruits)  # → False

# 数値のリスト演算
numbers = [10, 20, 30, 40, 50]
print(sum(numbers))   # → 150
print(max(numbers))   # → 50
print(min(numbers))   # → 10
