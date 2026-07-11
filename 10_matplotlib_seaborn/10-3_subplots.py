# ========================================
# 第10章: Matplotlib — Figure・Axes・保存
# ========================================

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y1 = [1, 3, 2, 4, 3]
y2 = [2, 1, 4, 2, 5]
categories = ['A', 'B', 'C']
values     = [10, 25, 15]
data       = np.random.randn(100)

# ===== サブプロット（2×2）=====

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x, y1)
axes[0, 0].set_title('折れ線')

axes[0, 1].scatter(x, y2)
axes[0, 1].set_title('散布図')

axes[1, 0].bar(categories, values)
axes[1, 0].set_title('棒グラフ')

axes[1, 1].hist(data, bins=15)
axes[1, 1].set_title('ヒストグラム')

plt.tight_layout()              # 自動レイアウト調整
plt.savefig('subplots.png', dpi=150)  # ファイルに保存
plt.show()
