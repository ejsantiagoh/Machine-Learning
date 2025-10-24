import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split  # Asumiendo sklearn disponible localmente; sino, usa manual split

# Crear DataFrame con datos "reales" (inspirados en diabetes dataset)
data = {
    'age': [0.038, -0.001, 0.046, -0.074, 0.042],  # Edad normalizada
    'bmi': [0.062, 0.062, -0.045, -0.057, 0.023],  # Índice de masa corporal
    'bp': [0.062, -0.019, -0.008, -0.043, 0.091],   # Presión sanguínea
    'target': [151, 75, 141, 206, 135]              # Progresión de diabetes (valor continuo)
}
df = pd.DataFrame(data)

# Explorar DataFrame
print(df.head())
print(df.describe())

# Preparar datos para ML
X = df.drop('target', axis=1).values.astype(np.float32)
y = df['target'].values.astype(np.float32).reshape(-1, 1)

# Split (buena práctica)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convertir a tensores
X_train_t = torch.from_numpy(X_train)
y_train_t = torch.from_numpy(y_train)
X_test_t = torch.from_numpy(X_test)
y_test_t = torch.from_numpy(y_test)

# "Pipeline" manual: Preprocesamiento (normalización manual)
mean = X_train_t.mean(dim=0)
std = X_train_t.std(dim=0)
X_train_t = (X_train_t - mean) / std
X_test_t = (X_test_t - mean) / std  # Usa train stats para evitar leakage

# Modelo PyTorch
model = nn.Linear(3, 1)  # 3 features a 1 output
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Entrenamiento
for epoch in range(200):
    optimizer.zero_grad()
    out = model(X_train_t)
    loss = criterion(out, y_train_t)
    loss.backward()
    optimizer.step()

# Evaluación
preds = model(X_test_t)
mse = criterion(preds, y_test_t).item()
print(f'MSE en test: {mse}')