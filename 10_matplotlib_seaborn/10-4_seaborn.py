# ========================================
# 第10章: Seaborn — 統計的可視化
# ========================================
# 実行: pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style='whitegrid', palette='muted')

df = pd.DataFrame({
    '点数': [85, 92, 78, 88, 76, 95, 83, 70],
    '合否': ['合格', '合格', '不合格', '合格', '不合格', '合格', '合格', '不合格'],
    '年齢': [25, 30, 22, 28, 21, 35, 27, 20]
})

# ===== ヒストグラム＋分布 =====

sns.histplot(df['点数'], kde=True)
plt.show()

# ===== 箱ひげ図 =====

sns.boxplot(x='合否', y='点数', data=df)
plt.show()

# ===== 散布図（回帰直線付き）=====

sns.regplot(x='年齢', y='点数', data=df)
plt.show()

# ===== カウントプロット =====

sns.countplot(x='合否', data=df)
plt.show()

# ===== ヒートマップ（相関行列）=====

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.show()

# ===== ペアプロット（全変数の関係）=====

sns.pairplot(df, hue='合否')
plt.show()
