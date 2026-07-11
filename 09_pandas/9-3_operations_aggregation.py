# ========================================
# 第9章-3: pandas — 欠損値処理・集計・加工・整形
# ========================================

import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / 'train.csv'
df = pd.read_csv(DATA)

# ===== 欠損値の確認 =====

print(df.isnull().sum())            # 列ごとの欠損数
print(df.isnull().mean().round(3))  # 列ごとの欠損割合

# ===== 欠損値の処理 =====

# 欠損値を含む行を削除
df_dropped = df.dropna()
print(df_dropped.shape)

# Age の欠損を中央値で補完
df['Age'] = df['Age'].fillna(df['Age'].median())

# Embarked の欠損を最頻値で補完
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Cabin は欠損が多いため 'Unknown' で補完
df['Cabin'] = df['Cabin'].fillna('Unknown')

print(df.isnull().sum())  # 補完後の確認

# ===== 基本統計量 =====

print(df['Fare'].sum())         # 合計
print(df['Age'].mean())         # 平均
print(df['Age'].median())       # 中央値
print(df['Fare'].max())         # 最大値
print(df['Fare'].min())         # 最小値
print(df.describe())            # 数値列の統計量を一括確認

# ===== 列の追加 =====

# 家族の人数（自分を含む）
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# 一人旅フラグ
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

print(df[['SibSp', 'Parch', 'FamilySize', 'IsAlone']].head())

# ===== 列・行の削除 =====

df = df.drop(columns=['Ticket', 'Cabin'])   # 不要列を削除
# df = df.drop(index=0)                     # 特定行を削除
print(df.columns)

# ===== 列名の変更 =====

df = df.rename(columns={
    'Survived': 'survived',
    'Pclass':   'pclass',
    'Age':      'age',
    'Fare':     'fare'
})
print(df.columns)

# ===== 整形 =====

# 重複行の削除
df = df.drop_duplicates()

# fare の降順で並び替え
print(df.sort_values('fare', ascending=False).head())

# インデックスを振り直す
df = df.reset_index(drop=True)
print(df.head())
