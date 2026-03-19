# ========================================
# 第5章: 戻り値
# ========================================

# --- 基本のreturn ---
def square(x):
    return x ** 2

result = square(5)
print(result)          # → 25
print(square(3) + 1)   # → 10 (戻り値をそのまま使える)

# --- returnがない関数はNoneを返す ---
def say_hello():
    print("Hello!")

say_hello()          # → Hello!
print(say_hello())   # → Hello! None (Hello!は関数内のprintで出力されるが、関数自体はNoneを返す)

# --- 真偽値を返す関数（is_で始める慣習）---
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # → True
print(is_even(7))   # → False

# if文と組み合わせて
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_list = [n for n in numbers if is_even(n)] #4-5_iterables.pyのevensと同じ
print(even_list)    # → [2, 4, 6, 8]

def is_passing(score, threshold=60):
    return score >= threshold

scores = [45, 72, 88, 55, 91, 63]
print([s for s in scores if is_passing(s)])  # → [72, 88, 91, 63]

# --- 複数の値を返す（タプルで返す）---
def min_max(lst):
    return min(lst), max(lst)   # タプルとして返す

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"最小: {low}, 最大: {high}")  # → 最小: 1, 最大: 9

# --- 早期return（ガード節）---
def divide(a, b):
    if b == 0:
        return None   # 0除算を防ぐ
    return a / b

print(divide(10, 2))   # → 5.0
print(divide(10, 0))   # → None

# --- 実践例 ---
# 成績評価
def evaluate(score):
    """点数を評価に変換する"""
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

test_scores = [95, 82, 76, 61, 48]
for s in test_scores:
    print(f"{s}点 → {evaluate(s)}")

#FizzBuzz問題
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:  # x % 15 == 0とも書ける
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

numbers = [3, 5, 30, 49]
for n in numbers:
    print(f"{n}: {fizz_buzz(n)}")
