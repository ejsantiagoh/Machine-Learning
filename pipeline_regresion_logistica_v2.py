from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pandas as pd

# Generar datos más realistas: 1000 muestras, 5 características, clasificación binaria
X, y = make_classification(n_samples=1000, n_features=5, n_informative=3, n_redundant=2, random_state=42)

# Convertir a DataFrame para simular datos reales (opcional, pero útil)
feature_names = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# Variables
X = df[feature_names]
y = df['target']

# División entrenamiento / prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 🔹 Crear pipeline
pipe = Pipeline([
    ('escalador', StandardScaler()),          # Paso 1: escalar datos
    ('modelo', LogisticRegression())          # Paso 2: modelo
])

# Para aumentar complejidad: Búsqueda de hiperparámetros con GridSearchCV
param_grid = {
    'modelo__C': [0.1, 1, 10],  # Regularización
    'modelo__solver': ['liblinear', 'lbfgs']
}

grid_search = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')

# Entrenar con búsqueda
grid_search.fit(X_train, y_train)

# Mejor modelo
best_model = grid_search.best_estimator_

# Evaluar
score = best_model.score(X_test, y_test)
best_params = grid_search.best_params_

print("Mejores parámetros:", best_params)
print("Precisión en prueba:", score)
