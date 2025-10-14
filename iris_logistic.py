import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# Cargar el dataset directamente desde la URL
url = 'https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv'
df = pd.read_csv(url)

# Filtrar para clasificación binaria (versicolor vs virginica)
df = df[df['species'].isin(['versicolor', 'virginica'])]

# Variables (ajustadas a los nombres de columnas del CSV)
y = (df['species'] == 'virginica').astype(int).values
X = df.drop('species', axis=1).values

# División manual entrenamiento/prueba (70/30)
np.random.seed(42)
indices = np.random.permutation(len(X))
split = int(0.7 * len(X))
X_train, X_test = X[indices[:split]], X[indices[split:]]
y_train, y_test = y[indices[:split]], y[indices[split:]]

# Escalado manual
mean = X_train.mean(axis=0)
std = X_train.std(axis=0)
X_train_scaled = (X_train - mean) / std
X_test_scaled = (X_test - mean) / std

# Convertir a tensores de PyTorch
X_train_t = torch.from_numpy(X_train_scaled).float()
y_train_t = torch.from_numpy(y_train).float()
X_test_t = torch.from_numpy(X_test_scaled).float()
y_test_t = torch.from_numpy(y_test).float()

# Definir modelo de regresión logística con PyTorch
class LogisticModel(nn.Module):
    def __init__(self, input_size):
        super(LogisticModel, self).__init__()
        self.linear = nn.Linear(input_size, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))

# Búsqueda de hiperparámetros (grid search simple sobre learning rate)
learning_rates = [0.01, 0.1, 1.0]
best_acc = 0
best_lr = None

for lr in learning_rates:
    model = LogisticModel(4)  # 4 features
    criterion = nn.BCELoss()  # Binary Cross Entropy Loss
    optimizer = optim.SGD(model.parameters(), lr=lr)
    
    # Entrenamiento
    for epoch in range(200):  # Más epochs para mejor convergencia
        optimizer.zero_grad()
        outputs = model(X_train_t).squeeze()
        loss = criterion(outputs, y_train_t)
        loss.backward()
        optimizer.step()
    
    # Evaluación
    with torch.no_grad():
        preds = (model(X_test_t).squeeze() > 0.5).float()
        acc = (preds == y_test_t).float().mean().item()
    
    if acc > best_acc:
        best_acc = acc
        best_lr = lr

# Resultados
print(f"Mejor learning rate: {best_lr}")
print(f"Precisión en prueba: {best_acc}")