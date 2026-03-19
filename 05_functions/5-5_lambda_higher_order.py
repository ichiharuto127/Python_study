# ========================================
# 第5章: ラムダ式・高階関数
# ========================================

# --- ラムダ式: 1行で書ける無名関数 ---
# lambda 引数: 式

double = lambda x: x * 2
print(double(5))     # → 10

add = lambda a, b: a + b
print(add(3, 7))     # → 10

# 条件式も使える
classify = lambda x: "正" if x > 0 else ("負" if x < 0 else "ゼロ")
print(classify(5))   # → 正
print(classify(-3))  # → 負
print(classify(0))   # → ゼロ

# --- 高階関数: 関数を引数や戻り値にする ---

# --- sorted() の key にラムダを使う ---
players = [
    {"name": "田中", "goals": 20, "assists": 8},
    {"name": "鈴木", "goals": 8,  "assists": 15},
    {"name": "佐藤", "goals": 15, "assists": 12},
]

# ゴール数で降順
by_goals = sorted(players, key=lambda p: p["goals"], reverse=True)
for p in by_goals:
    print(f"{p['name']}: {p['goals']}G")

print("===")

# ゴール+アシストの合計で降順
by_total = sorted(players, key=lambda p: p["goals"] + p["assists"], reverse=True)
for p in by_total:
    print(f"{p['name']}: {p['goals'] + p['assists']}pts")

# --- map(): 全要素に関数を適用 ---
nums = [1, 2, 3, 4, 5]

# 関数を渡す
squared = list(map(lambda x: x / 2, nums))
print(squared)   # → [0.5, 1.0, 1.5, 2.0, 2.5]

# 既存の関数を渡す
print(list(map(int, squared)))   # → [0, 1, 1, 2, 2]

# --- filter(): 条件を満たす要素を抽出 ---
scores = [45, 72, 88, 55, 91, 63, 70]
passing = list(filter(lambda s: s >= 70, scores))
print(passing)   # → [72, 88, 91, 70]

# --- 関数を返す関数（クロージャ）---
def make_multiplier(n):
    """n倍にする関数を作る"""
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # → 10
print(triple(5))   # → 15

# 消費税計算機を作る
def make_tax_calculator(rate):
    return lambda price: int(price * (1 + rate))

tax10 = make_tax_calculator(0.10)
print(f"税込(10%): {tax10(1000)}円")   # → 1100円
