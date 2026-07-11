# ========================================
# 第11章: scikit-learn — データ分割・前処理
# ========================================
# 実行: pip install scikit-learn

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# ===== サンプルデータ =====

df = pd.DataFrame({
    'feature1': [1.0, 2.0, 3.0, 4.0, 5.0],
    'feature2': [10.0, 8.0, 6.0, 4.0, 2.0],
    'label':    ['A', 'B', 'A', 'B', 'A']
})

X = df[['feature1', 'feature2']].values
y = df['label'].values

# ===== 訓練・テスト分割（8:2）=====

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"訓練: {X_train.shape}, テスト: {X_test.shape}")

# ===== 標準化（平均0・分散1）=====

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)   # 訓練データでfitして変換
X_test  = scaler.transform(X_test)         # テストデータは変換のみ

print(f"訓練の平均: {X_train.mean(axis=0).round(3)}")
print(f"訓練の標準偏差: {X_train.std(axis=0).round(3)}")

# ===== ラベルエンコーディング（カテゴリ→数値）=====

le = LabelEncoder()
y_encoded = le.fit_transform(y)
print(f"元ラベル: {y}")
print(f"エンコード後: {y_encoded}")
print(f"対応: {le.classes_}")
