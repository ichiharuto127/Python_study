# ========================================
# 第11章: scikit-learn — モデルの評価
# ========================================

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)

# ===== データ準備 =====

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ===== 精度 =====

print(f"精度: {accuracy_score(y_test, y_pred):.4f}")

# ===== 詳細レポート（適合率・再現率・F1スコア）=====

print(classification_report(y_test, y_pred, target_names=iris.target_names))

# ===== 混同行列 =====

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.xlabel('予測')
plt.ylabel('正解')
plt.title('混同行列')
plt.show()

# ===== 交差検証 =====

scaler2 = StandardScaler()
X_scaled = scaler2.fit_transform(X)

scores = cross_val_score(model, X_scaled, y, cv=5)
print(f"CV精度: {scores.mean():.4f} ± {scores.std():.4f}")
