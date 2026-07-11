# ========================================
# 第9章-7: pandas — 時系列データの操作
# ========================================
# タイタニックは時系列データを持たないため疑似的な株価データを使用

import pandas as pd
import numpy as np

# ===== pd.date_range() — 日付の生成 =====

dates = pd.date_range(start='2024-01-01', periods=60, freq='D')
print(dates[:5])

# ===== 時系列 DataFrame の作成 =====

np.random.seed(42)
df = pd.DataFrame({
    'date':  dates,
    'price': np.random.randint(2800, 3200, size=60).astype(float),
    'volume': np.random.randint(100, 500, size=60)
})
print(df.head())

# ===== set_index() — 日付列をインデックスに設定 =====

df = df.set_index('date')
print(df.head())

# ===== resample() — 月次集計 =====

# 月ごとの平均株価
monthly_mean = df['price'].resample('ME').mean()
print(monthly_mean)

# 月ごとの合計出来高
monthly_volume = df['volume'].resample('ME').sum()
print(monthly_volume)

# ===== shift() — 前日比の計算 =====

df['prev_price'] = df['price'].shift(1)          # 1日前の価格
df['daily_return'] = df['price'] - df['prev_price']  # 前日比（差分）
df['pct_change'] = df['price'].pct_change()      # 前日比（変化率）
print(df.head(10))

# ===== rolling() — 移動平均 =====

df['ma5']  = df['price'].rolling(window=5).mean()   # 5日移動平均
df['ma20'] = df['price'].rolling(window=20).mean()  # 20日移動平均
print(df[['price', 'ma5', 'ma20']].tail(20))
