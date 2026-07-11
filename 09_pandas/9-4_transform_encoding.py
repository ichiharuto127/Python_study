# ========================================
# 第9章-4: pandas — 値の変換・カテゴリ変数・エンコーディング
# ========================================

import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / 'train.csv'
df = pd.read_csv(DATA)
df['Age'] = df['Age'].fillna(df['Age'].median())

# ===== map() による値の変換 =====

# 辞書を使ってカテゴリを数値に変換
df['Sex_num'] = df['Sex'].map({'male': 0, 'female': 1})
print(df[['Sex', 'Sex_num']].head())

# ===== replace() による値の置換 =====

# 乗船港コードを都市名に置換
df['Embarked'] = df['Embarked'].fillna('S')
df['Embarked_name'] = df['Embarked'].replace({
    'S': 'Southampton',
    'C': 'Cherbourg',
    'Q': 'Queenstown'
})
print(df[['Embarked', 'Embarked_name']].head())

# ===== apply() + lambda による列変換 =====

# 年齢カテゴリ列を追加
df['AgeGroup'] = df['Age'].apply(
    lambda x: 'child' if x < 18 else ('senior' if x >= 60 else 'adult')
)
print(df[['Age', 'AgeGroup']].head(10))

# ===== 文字列操作（str アクセサ）=====

# 名前をすべて大文字に
df['Name_upper'] = df['Name'].str.upper()

# 名前をすべて小文字に
df['Name_lower'] = df['Name'].str.lower()

print(df[['Name', 'Name_upper', 'Name_lower']].head(3))

# ===== ワンホットエンコーディング（get_dummies）=====

# 機械学習の入力用にカテゴリ変数を 0/1 に変換
df_dummies = pd.get_dummies(df, columns=['Embarked'], dtype=int)
print(df_dummies[['Embarked_S', 'Embarked_C', 'Embarked_Q']].head())

# ===== カテゴリの傾向確認 =====

# ユニークな値の取得
print(df['Pclass'].unique())        # → [3 1 2]

# 出現頻度（降順）
print(df['Pclass'].value_counts())

# 特定の値が含まれるか確認（isin）
print(df[df['Pclass'].isin([1, 2])][['Name', 'Pclass']].head())
