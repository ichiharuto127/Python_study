# ========================================
# 第9章-5: pandas — データ結合・グループ集計・ピボット
# ========================================

import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / 'train.csv'
df = pd.read_csv(DATA)

# ===== pd.concat() — 縦結合 =====

df_top    = df.iloc[:100]
df_bottom = df.iloc[100:200]
df_concat = pd.concat([df_top, df_bottom], ignore_index=True)
print(df_concat.shape)  # → (200, 12)

# ===== pd.merge() — 横結合（共通キーで結合）=====

# 乗客基本情報と運賃情報を分けて結合する例
df_info = df[['PassengerId', 'Name', 'Sex', 'Age']]
df_fare = df[['PassengerId', 'Pclass', 'Fare', 'Survived']]

# 内部結合（デフォルト）：両方に存在するキーのみ
df_inner = pd.merge(df_info, df_fare, on='PassengerId')
print(df_inner.head())

# 左外部結合：左のデータを全行残す
df_left = pd.merge(df_info, df_fare, on='PassengerId', how='left')
print(df_left.shape)

# ===== groupby() — グループ集計 =====

# チケットクラス別の平均生存率
print(df.groupby('Pclass')['Survived'].mean())

# 性別ごとの生存率
print(df.groupby('Sex')['Survived'].mean())

# 複数の集計を一度に（agg）
print(
    df.groupby('Pclass').agg(
        生存率=('Survived', 'mean'),
        平均年齢=('Age', 'mean'),
        平均運賃=('Fare', 'mean'),
        人数=('PassengerId', 'count')
    ).round(2)
)

# ===== unstack() — クロス集計を見やすく =====

# 性別 × クラス別の平均生存率
cross = df.groupby(['Sex', 'Pclass'])['Survived'].mean().unstack()
print(cross.round(2))

# ===== pivot_table() — ピボットテーブル =====

pivot = pd.pivot_table(
    df,
    values='Survived',
    index='Sex',
    columns='Pclass',
    aggfunc='mean'
)
print(pivot.round(2))
