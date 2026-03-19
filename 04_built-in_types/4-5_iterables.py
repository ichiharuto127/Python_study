# ========================================
# 第4章: 反復可能オブジェクト・順序を持つオブジェクト
# ========================================

# 反復可能(iterable)なオブジェクト = for文で使えるオブジェクト
# str, list, tuple, dict, set, range など

# --- zip: 複数のイテラブルを同時に回す ---
names   = ["田中", "鈴木", "佐藤"]
numbers = [10, 7, 3]
positions = ["FW", "MF", "DF"]

for name, num, pos in zip(names, numbers, positions):
    print(f"{num} {name} ({pos})")
# → 10 田中 (FW)
# → 7  鈴木 (MF)
# → 3  佐藤 (DF)

# --- enumerate: インデックスと値を同時に ---
fruits = ["りんご", "みかん", "ぶどう"]
for i, fruit in enumerate(fruits, start=1):  # start=1 で1から始める
    print(f"{i}. {fruit}")
# → 1. りんご
# → 2. みかん
# → 3. ぶどう

# --- map: 全要素に関数を適用 ---
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# lambdaはユーザー定義関数。xを受け取ってx**2を返す関数を定義している。

print(squared)  # → [1, 4, 9, 16, 25]

# str のリストを int に一括変換
str_nums = ["10", "20", "30"]
int_nums = list(map(int, str_nums))
print(int_nums)  # → [10, 20, 30]

# --- filter: 条件を満たす要素だけ抽出 ---
scores = [55, 72, 88, 43, 91, 67, 78]
passing = list(filter(lambda x: x >= 70, scores))
# xを受け取ってx >= 70を返す関数を定義している。70以上の要素だけ残る。
print(passing)  # → [72, 88, 91, 78]

# --- sorted のkeyオプション ---
players = [
    {"name": "田中", "goals": 20},
    {"name": "鈴木", "goals": 8},
    {"name": "佐藤", "goals": 15},
]
# ゴール数で降順ソート
sorted_players = sorted(players, key=lambda p: p["goals"], reverse=True)
# pを受け取ってp["goals"]を返す関数を定義している。reverse=Trueで降順になる。
for p in sorted_players:
    print(f"{p['name']}: {p['goals']}ゴール")
# → 田中: 20ゴール
# → 佐藤: 15ゴール
# → 鈴木: 8ゴール

# --- リスト内包表記（応用）---
# 基本
evens = [x for x in range(10) if x % 2 == 0]
# xを受け取ってxが2の倍数であるかを判定し、Trueのときだけxをリストに入れる。
print(evens)  # → [0, 2, 4, 6, 8]

# 2次元: 掛け算表
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
# i,jを受け取ってi*jを計算する関数を定義している。二重の内包表記で2次元リストができる。
print(table)
# 1*1から5*5までの掛け算表ができる。

# 辞書内包表記
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # → {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 集合内包表記
unique_lengths = {len(fruit) for fruit in fruits}
print(unique_lengths) # → {3} （すべての果物の名前の長さが3文字なので、集合は{3}になる）
