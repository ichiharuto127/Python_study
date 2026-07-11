# ========================================
# 第11章: scikit-learn — 教師なし学習
# ========================================

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# ===== データ準備 =====

iris = load_iris()
X = iris.data

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ===== k-means クラスタリング =====

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

labels  = kmeans.labels_
centers = kmeans.cluster_centers_

print(f"クラスタラベル: {labels}")

# ===== 次元削減 (PCA) =====

pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)

print(f"説明分散比: {pca.explained_variance_ratio_}")
print(f"累積寄与率: {pca.explained_variance_ratio_.sum():.4f}")

# ===== クラスタリング結果を2次元で可視化 =====

plt.figure(figsize=(8, 6))
for cluster in range(3):
    mask = labels == cluster
    plt.scatter(X_2d[mask, 0], X_2d[mask, 1], label=f'クラスタ{cluster}', alpha=0.7)

plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('k-means クラスタリング（PCA 2次元投影）')
plt.legend()
plt.show()
