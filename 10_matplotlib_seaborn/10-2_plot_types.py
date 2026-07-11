# ========================================
# 第10章: Matplotlib — グラフの種類
# ========================================

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

# ===== 散布図 =====

plt.scatter(x, y, c='blue', s=50, alpha=0.7)
plt.title('散布図')
plt.show()

# ===== 棒グラフ =====

plt.bar(['A', 'B', 'C'], [10, 25, 15], color='steelblue')
plt.title('棒グラフ')
plt.show()

# ===== 水平棒グラフ =====

plt.barh(['A', 'B', 'C'], [10, 25, 15])
plt.title('水平棒グラフ')
plt.show()

# ===== ヒストグラム =====

data = np.random.randn(200)
plt.hist(data, bins=20, color='green', edgecolor='black')
plt.title('ヒストグラム')
plt.show()

# ===== 円グラフ =====

plt.pie([30, 25, 45], labels=['A', 'B', 'C'], autopct='%1.1f%%')
plt.title('円グラフ')
plt.show()

# ===== エラーバー付き棒グラフ =====

means = [10, 20, 15]
stds  = [1, 2, 1.5]
plt.bar(['A', 'B', 'C'], means, yerr=stds, capsize=5)
plt.title('エラーバー付き棒グラフ')
plt.show()
