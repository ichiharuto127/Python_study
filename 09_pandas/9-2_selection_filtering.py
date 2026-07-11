# ========================================
# 第9章-2: pandas — データ確認・選択・フィルタリング・型変換
# ========================================

import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / 'train.csv'
df = pd.read_csv(DATA)

# ===== データの全体像把握 =====

print(df.shape)     # (行数, 列数) → (891, 12)
print(df.dtypes)    # 各列のデータ型
print(df.info())    # 欠損値・メモリ使用量を含む概要
print(df.head())    # 先頭5行
print(df.tail(3))   # 末尾3行

# ===== 列の選択 =====

print(df['Age'])                        # 1列 → Series
print(df[['Name', 'Sex', 'Pclass']])    # 複数列 → DataFrame

# ===== 行の選択（loc / iloc）=====

print(df.loc[0])                            # ラベル0の行
print(df.iloc[2])                           # インデックス番号2の行
print(df.loc[0:2, 'Name':'Age'])            # 行・列の範囲（ラベル指定）
print(df.iloc[0:3, 1:5])                    # 行・列の範囲（番号指定）

# ===== 条件フィルタリング =====

# 生存者のみ
print(df[df['Survived'] == 1])

# 30歳以上
print(df[df['Age'] >= 30])

# &（かつ）：1等かつ女性
print(df[(df['Pclass'] == 1) & (df['Sex'] == 'female')])

# |（または）：1等または2等
print(df[(df['Pclass'] == 1) | (df['Pclass'] == 2)])

# query() による絞り込み（可読性が高い）
print(df.query('Pclass == 1 and Sex == "female"'))
print(df.query('Age >= 18 and Survived == 1'))

# ===== データ型の変換（astype）=====

# メモリ節約のため int64 → int8 に変換
df['Survived'] = df['Survived'].astype('int8')
df['Pclass']   = df['Pclass'].astype('int8')
print(df[['Survived', 'Pclass']].dtypes)

# カテゴリ型に変換（文字列の繰り返しが多い列に有効）
df['Sex']      = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')
print(df[['Sex', 'Embarked']].dtypes)
