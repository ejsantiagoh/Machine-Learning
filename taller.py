# Taller Integrado 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

# Crear dataset base
datos = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "nombre": ["Ana", "Luis", "Carlos", "Diana", "Mateo", "Sofía", "Pedro", "Laura", "Andrés", "Camila"],
    "horas_estudio": [1, 2, 3, 4, 5, 6, 2, 7, 3, 8],
    "participaciones": [2, 3, 4, 5, 5, 6, 2, 7, 3, 8],
    "nota_final": [45, 50, 55, 60, 65, 70, 48, 75, 58, 80]
}

df = pd.DataFrame(datos)

# Se guarda como csv
df.to_csv("estudiantes.csv", index=False)
print("Archivo estudiantes.csv creado con exito")

# print(df.head()) # Se visualiza las primeras 5 lineas
# print(df.tail(10)) # se visualiza según la cantidad indicada
# print(df.describe()) # para visualizar metricas 
# print(df.shape) # se visualiza el tamaño del df
# print(df[['nombre','horas_estudio']]) # se visualiza segun las columnas
# print(df.columns) # muestra el nombre de las columnas
# print(df.columns.tolist())
# print(type(df.columns))
# df = df[[ 'nombre','horas_estudio']] # Se puede cambiar el orden de las columnas
# df['promedio'] = (df['participaciones'] + df['nota_final']) / 2 # se agrega una nueva columna
# print(df.tail(10))

# # Cargar dataset
data = pd.read_csv("estudiantes.csv")



