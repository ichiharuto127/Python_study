# ========================================
# 第10章: Matplotlib — 基本プロット
# ========================================
# 実行: pip install matplotlib

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'MS Gothic'  # Windowsの日本語フォント

# ===== 折れ線グラフ =====

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

plt.plot(x, y)
plt.title('タイトル')
plt.xlabel('X軸')
plt.ylabel('Y軸')
plt.grid(True)
plt.show()

# ===== 複数の線・凡例 =====

y1 = [1, 3, 2, 4, 3]
y2 = [2, 1, 4, 2, 5]

plt.plot(x, y1, label='データ1', color='blue', linestyle='--', marker='o')
plt.plot(x, y2, label='データ2', color='red')
plt.legend()    # 凡例
plt.show()
