import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandasgui import show
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Crear datos ficticios
n = 100 #numero de muestras

# Generar valores para la cantidad de fertilizante (x) en un rango de 0 a 100kg
np.random.seed(42) #reproducibilidad
fertilizante = np.random.uniform(0, 100, n)

# Definir una relacion lineal con ruido aleatorio para la cantidad de papas (Y)
# Suponemos que por cada 1kg de fertilizante obtendremos 0.8 toneladas
# Y agregamos un poco de ruido normal para simular variedad natural

papas = 0.8 * fertilizante + np.random.normal(0,5, n) + 8 #Intercepto en 8

df = pd.DataFrame({
    'Fertilizante (Kg)': fertilizante,
    'Papas (toneladas)': papas
})

# print(df.head()) #Muestra las primeras filas del dataset
# print(df.info()) # Información sobre las columnas y tipos de datos
# print(df.describe()) # Estadisticas descriptivas para columnas numericas

x = df[['Fertilizante (Kg)']].values
y = df['Papas (toneladas)'].values

# show(df) #muestra los datos con pandasgui

# Separar los datos de entrenamiento

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Definir nuestro modelo y entrenarlo 
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Hacer prediccion
y_pred = regressor.predict(X_test)

# calcular b0 y b1
b1 = regressor.coef_[0]
b0 = regressor.intercept_

print(f"""
    b1:{b1}, 
    b0:{b0}
    """)

# Evaluacion: Calcular el MSE, RMSE, R^2
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"""
    mse: {mse},
    rmse:{rmse},
    r2:{r2}
    """)

plt.figure(figsize=(7,4))

# Scatter plot del set de entrenamiento
plt.scatter(X_train, y_train, color="blue", label="Datos de entrenamiento")

plt.scatter(X_test, y_test, color="green", label="Datos de prueba")

plt.plot(X_train, regressor.predict(X_train), color="red", label="Linea de regresion")

plt.title("Regresión lineal: Fertilizante vs Producción de papas")
plt.xlabel("Fertilizante (Kg)")
plt.ylabel("Papas (toneladas)")
plt.legend()

plt.show()
