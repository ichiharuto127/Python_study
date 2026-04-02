# ========================================
# 第8章: NumPy — 数学的関数・集計
# ========================================

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

# ===== 集計関数 =====

print(np.sum(a))                 # →21（全体合計）
print(np.sum(a, 0))              # →[5, 7, 9]（行方向に合計）
print(np.sum(a, 1))              # →[6, 15]（列方向に合計）
print(np.concatenate([a, b], 0)) # 行方向に結合
print(np.concatenate([a, b], 1)) # 列方向に結合

# ===== 統計関数 =====

print(np.mean(a))           # →3.5 （平均値）
print(np.max(a))            # →6 （最大値）
print(np.min(a))            # →1 （最小値）
print(np.argmax(a))         # →5（1次元配列に平坦化したときの最大値のインデックス）
print(np.argmin(a))         # →0（1次元配列に平坦化したときの最小値のインデックス）
print(np.std(a))            # →1.707825127659933（標準偏差）
print(np.var(a))            # →2.9166666666666665（分散）

# ===== 数学的関数 =====

print(np.sqrt(a))           # 各要素の平方根
print(np.log(a))            # 各要素の自然対数
print(np.exp(a))            # 各要素の指数関数
print(np.abs(np.array([-1, -2, 3])))   # →[1, 2, 3] （絶対値）

# ===== ソート =====

c = np.array([3, 1, 4, 1, 5, 9, 2])
print(np.sort(c))           # → [1, 1, 2, 3, 4, 5, 9]
print(np.argsort(c))        # → ソート後のインデックス

# ===== ユニーク =====

print(np.unique(c))         # → [1, 2, 3, 4, 5, 9]
