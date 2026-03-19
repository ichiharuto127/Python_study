# ========================================
# 第5章: 引数・デフォルト引数
# ========================================

# --- 基本の引数 ---
def greet(name):
    print(f"こんにちは、{name}さん！")

greet("田中")   # → こんにちは、田中さん！
greet("鈴木")   # → こんにちは、鈴木さん！

# --- 複数の引数 ---
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(10, 5)   # → 10 + 5 = 15
add(3, 7)    # → 3 + 7 = 10

# --- デフォルト引数（省略できる引数）---
def greet_with_title(name, title="さん"):
    print(f"こんにちは、{name}{title}！")

greet_with_title("田中")         # → こんにちは、田中さん！
greet_with_title("田中", "先生") # → こんにちは、田中先生！

# デフォルト引数は末尾に置く（ルール）
def power(base, exponent=2):   # デフォルトは2乗
    return base ** exponent

print(power(3))     # → 9  (3の2乗)
print(power(3, 3))  # → 27 (3の3乗)

# --- キーワード引数（名前を指定して渡す）---
def player_info(name, number, position):
    print(f"{number} {name} ({position})")

player_info("田中", 10, "FW")                         # → 10 田中 (FW) 位置引数
player_info(name="鈴木", position="MF", number=7)     # → 7 鈴木 (MF) キーワード引数（順序自由）

# --- 可変長引数: *args ---
def total(*args):
    print(f"受け取った引数: {args}")   # タプルとして受け取る
    return sum(args)

print(total(1, 2, 3))          # → 6
print(total(10, 20, 30, 40))   # → 100

# --- 可変長キーワード引数: **kwargs ---
def profile(**kwargs):
    print(f"受け取ったキーワード引数: {kwargs}")  # 辞書として受け取る
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(name="田中", age=20, sport="サッカー", position="FW")