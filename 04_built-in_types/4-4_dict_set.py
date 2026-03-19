# ========================================
# 第4章: 辞書・集合
# ========================================

# ===== 辞書（dict）: KeyとValueのペア =====

player = {
    "name": "田中",
    "number": 10,
    "position": "FW",
    "goals": 15
}

# 値の取得
print(player["name"])           # → 田中 （Keyを入れるとValueを返す）
print(player.get("goals"))      # → 15
print(player.get("assists"))    # → None （KeyがなければNone）
print(player.get("assists", 0)) # → 0 （Keyがなければ0）

# 値の追加・変更
player["assists"] = 8           # 新しいKeyを追加
player["goals"] = 20            # 既存のValueを変更
print(player)
player2 = {
    "assists": 10,
    "age": 28
}                               # 別の辞書をupdate()で結合
player.update(player2)          # playerにplayer2の内容を追加・上書き
print(player)

# 削除
del player["number"]            # Keyを指定して削除
print(player)

popped = player.pop("position") # Valueを取り出しながらKeyを削除
print(popped)                   # → FW

# キー・値・ペアの一覧
print(player.keys())    # → dict_keys(['name', 'goals', 'assists']) Keyの一覧
print(player.values())  # → dict_values(['田中', 20, 8]) Valueの一覧
print(player.items())   # → dict_items([...])

# for文で全要素を取得
for key, value in player.items():
    print(key, value)

# in演算子（キーの存在確認）
print("name" in player)   # → True
print("number" in player) # → False

# --- 辞書のリスト（よく使うパターン）---
team = [
    {"name": "田中", "goals": 20},
    {"name": "鈴木", "goals": 15},
    {"name": "佐藤", "goals": 10},
]
for p in team:
    print(f"{p['name']}: {p['goals']}ゴール")

# ===== 集合（set）: 重複なし・順序なし =====

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# 集合演算
print(a | b)   # → {1, 2, 3, 4, 5, 6, 7}   和集合
print(a & b)   # → {3, 4, 5}               積集合（共通部分）
print(a - b)   # → {1, 2}                  差集合（aだけ）
print(a ^ b)   # → {1, 2, 6, 7}            対称差（どちらか片方のみ）

# 重複を除去するテクニック
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(numbers))   # set()で重複を除去してからlist()でリストに戻す
print(unique)                 # → [1, 2, 3, 4]（順序は保証されない）

# 要素の追加・削除
s = {10, 20, 30}
s.add(40)
s.discard(20)
print(sorted(s))  # → [10, 30, 40]（setは順序なしなのでソートして表示）