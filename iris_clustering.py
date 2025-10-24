import pandas as pd
import numpy as np
from torch import tensor  # Para compatibilidad, pero usamos NumPy para clustering simple
import io

# Simular carga desde CSV (datos reales de Iris sample)
csv_data = """sepal_length,sepal_width,petal_length,petal_width
5.1,3.5,1.4,0.2
4.9,3.0,1.4,0.2
7.0,3.2,4.7,1.4
6.4,3.2,4.5,1.5
6.3,3.3,6.0,2.5
5.8,2.7,5.1,1.9
"""

df = pd.read_csv(io.StringIO(csv_data))

# Explorar
print(df.head())
print(df.describe())

# Preparar datos
X = df.values.astype(np.float32)

# K-Means simple (desde cero, como ejemplo previo)
def kmeans(X, k=2, max_iters=100):
    np.random.seed(42)
    centroids = X[np.random.choice(len(X), k, replace=False)]
    for _ in range(max_iters):
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        new_centroids = np.array([X[labels == i].mean(0) if len(X[labels == i]) > 0 else centroids[i] for i in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return labels, centroids

labels, centroids = kmeans(X, 3)  # 3 clusters para Iris
print('Labels:', labels)
print('Centroids:', centroids)