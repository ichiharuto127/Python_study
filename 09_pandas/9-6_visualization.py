# ========================================
# 第9章-6: pandas — データ可視化（plot）
# ========================================
# 実行: pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).parent / 'train.csv'
df = pd.read_csv(DATA)

# ===== 棒グラフ（bar）— カテゴリごとの件数・割合 =====

# クラス別の乗客数
df['Pclass'].value_counts().sort_index().plot(kind='bar', title='クラス別乗客数')
plt.xlabel('Pclass')
plt.ylabel('人数')
plt.tight_layout()
plt.show()

# クラス × 性別 の生存率（積み上げ棒グラフ）
df.groupby(['Pclass', 'Sex'])['Survived'].mean().unstack().plot(
    kind='bar', title='クラス×性別 生存率'
)
plt.ylabel('生存率')
plt.tight_layout()
plt.show()

# ===== ヒストグラム（hist）— 数値の分布 =====

df['Age'].dropna().plot(kind='hist', bins=20, title='年齢分布')
plt.xlabel('Age')
plt.tight_layout()
plt.show()

df['Fare'].plot(kind='hist', bins=40, title='運賃分布')
plt.xlabel('Fare')
plt.tight_layout()
plt.show()

# ===== 箱ひげ図（box）— 詳細な分布・外れ値の把握 =====

# クラス別の運賃分布
df.boxplot(column='Fare', by='Pclass')
plt.title('クラス別 運賃の分布')
plt.suptitle('')  # 自動タイトルを消す
plt.tight_layout()
plt.show()

# クラス別の年齢分布
df.boxplot(column='Age', by='Pclass')
plt.title('クラス別 年齢の分布')
plt.suptitle('')
plt.tight_layout()
plt.show()
