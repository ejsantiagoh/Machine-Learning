from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Cargar dataset Iris
iris = datasets.load_iris()
X = iris.data

# Aplicar KMeans con 3 clusters (reproducible)
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Calcular Silhouette Score
score = silhouette_score(X, labels)
print(f'Silhouette Score: {score}')