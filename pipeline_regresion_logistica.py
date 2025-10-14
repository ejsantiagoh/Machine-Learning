import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Datos simples
datos = {
    "edad": [20, 25, 30, 35, 40, 45],
    "salario": [2000, 2500, 3000, 4000, 5000, 6000],
    "compra": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(datos)

# Variables
X = df[["edad", "salario"]]
y = df["compra"]

# División entrenamiento / prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 🔹 Crear pipeline
pipe = Pipeline([
    ('escalador', StandardScaler()),          # Paso 1: escalar datos
    ('modelo', LogisticRegression())          # Paso 2: modelo
])

# Entrenar
pipe.fit(X_train, y_train)

# Evaluar
score = pipe.score(X_test, y_test)
print("Precisión:", score)
