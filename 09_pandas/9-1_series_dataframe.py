# ========================================
# 第9章-1: pandas — Series・DataFrame・入出力
# ========================================
# 実行: pip install pandas

import pandas as pd
import numpy as np
from pathlib import Path

DATA = Path(__file__).parent / 'train.csv'

# ===== Series の基本 =====

s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)            # ラベル付き1次元配列
print(s['b'])       # →20 ラベルで取得
print(s[1:3])       # →b:20, c:30 スライス
print(s[s > 15])    # →b:20, c:30, d:40 条件抽出

# ===== DataFrame の作成（辞書から）=====

sample = pd.DataFrame({
    'name': ['佐藤', '鈴木', '田中'],
    'age':  [25, 30, 22],
    'fare': [7.25, 71.28, 13.00]
})
print(sample)

# ===== CSV の読み込み =====

df = pd.read_csv(DATA)
print(df)

# エンコーディング・インデックス列を指定する場合
# df = pd.read_csv(DATA, encoding='utf-8', index_col=0)

# ===== Excel の読み込み（参考）=====

# df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# ===== ファイルへの出力 =====

# 加工後のデータを保存する
# df.to_csv('output.csv', index=False)
# df.to_excel('output.xlsx', index=False)
