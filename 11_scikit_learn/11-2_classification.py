# ========================================
# 第11章: scikit-learn — 分類モデル
# ========================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# ===== データ準備（Irisデータセット）=====

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ===== 各モデルの学習・評価 =====

models = {
    'k-NN':             KNeighborsClassifier(n_neighbors=5),
    'ロジスティック回帰': LogisticRegression(max_iter=1000),
    '決定木':           DecisionTreeClassifier(max_depth=5, random_state=42),
    'ランダムフォレスト': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM':              SVC(kernel='rbf', C=1.0),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{name}: {score:.4f}")
