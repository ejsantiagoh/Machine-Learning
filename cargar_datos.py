from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

# Cargar dataset
data = pd.read_csv("estudiantes.csv")

# Variables independientes (X) y dependiente (y)
X = data[["horas_estudio", "participaciones"]]
y = data["nota_final"]

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamiento
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Evaluación
predicciones = modelo.predict(X_test)
print("Precisión:", r2_score(y_test, predicciones))