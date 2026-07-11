# ========================================
# 第11章: scikit-learn — 回帰モデル
# ========================================

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# ===== データ準備 =====

housing = fetch_california_housing()
X, y = housing.data, housing.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ===== 各モデルの学習・評価 =====

models = {
    '線形回帰':          LinearRegression(),
    'リッジ（L2正則化）': Ridge(alpha=1.0),
    'ラッソ（L1正則化）': Lasso(alpha=0.1),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2  = r2_score(y_test, y_pred)
    print(f"{name}: MSE={mse:.4f}, R²={r2:.4f}")
