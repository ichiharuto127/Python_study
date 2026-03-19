# ========================================
# 第4章: リスト・タプル操作
# ========================================

# ===== リスト =====

scores = [78, 92, 65, 88, 71]

# 基本操作
print(len(scores))       # → 5
print(max(scores))       # → 92
print(min(scores))       # → 65
print(sum(scores))       # → 394

# 追加・削除
scores.append(95)        # 末尾に追加
print(scores)            # → [78, 92, 65, 88, 71, 95]

scores.insert(0, 100)    # 先頭に挿入
print(scores)            # → [100, 78, 92, 65, 88, 71, 95]

scores.remove(65)        # 値を指定して削除
print(scores)            # → [100, 78, 92, 88, 71, 95]

popped = scores.pop()    # 末尾を取り出す
print(popped)            # → 95
print(scores)            # → [100, 78, 92, 88, 71]

popped_idx = scores.pop(0)  # インデックス指定
print(popped_idx)        # → 100

# ソート
scores.sort()            # 昇順（元のリストを変更）
print(scores)            # → [71, 78, 88, 92]

scores.sort(reverse=True) # 降順
print(scores)            # → [92, 88, 78, 71]

sorted_scores = sorted(scores)  # 新しいリストを返す（元は変わらない）
print(sorted_scores)     # → [71, 78, 88, 92]

# 検索
print(scores.index(88))  # → 1 （インデックスを返す）
print(scores.count(88))  # → 1 （出現回数）

# コピー
a = [1, 2, 3]
b = a.copy()     # 浅いコピー（独立したリスト）
b.append(4)      # bに4を追加
a.extend(b)      # aにbの要素を追加（extend()はNoneを返す）
print(a)         # → [1, 2, 3, 1, 2, 3, 4]  （aは変更される）
print(b)         # → [1, 2, 3, 4]

# --- 2次元リスト（行列）---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])   # → 6  （インデックスは0から始まるので1行2列目 実際の行列では2行3列目）

for row in matrix:
    print(row)

# ===== タプル（変更不可） =====

point = (10, 20)      # 座標など、変わらないデータに使う。()は省略可能
print(point[0])       # → 10
print(point[1])       # → 20

# アンパック（複数変数への同時代入）
x, y = point
print(x, y)  # → x=10, y=20

# 関数の複数の戻り値もタプルで受け取れる
rgb = (255, 128, 0)
r, g, b = rgb
print(f"R:{r} G:{g} B:{b}")

# リストとタプルの変換
lst = list(point)    # タプル → リスト
tpl = tuple(scores)  # リスト → タプル
print(type(lst), type(tpl))
