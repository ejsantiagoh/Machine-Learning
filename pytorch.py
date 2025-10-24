# import torch
# import torch.nn as nn
# import torch.optim as optim
# import numpy as np
# import matplotlib.pyplot as plt

# # Datos sintéticos
# np.random.seed(42)
# X_np = np.arange(0, 10, dtype=np.float32).reshape(-1, 1)
# y_np = 2 * X_np + 1 + np.random.randn(10, 1).astype(np.float32) * 0.5
# X = torch.from_numpy(X_np)
# y = torch.from_numpy(y_np)

# # Modelo
# model = nn.Linear(1, 1)
# criterion = nn.MSELoss()
# optimizer = optim.SGD(model.parameters(), lr=0.01)

# # Entrenamiento expandido (más épocas para mejor convergencia)
# losses = []
# for epoch in range(200):  # Expandido de 100 a 200
#     optimizer.zero_grad()
#     out = model(X)
#     loss = criterion(out, y)
#     loss.backward()
#     optimizer.step()
#     losses.append(loss.item())
#     if epoch % 50 == 0:
#         print(f'Epoch {epoch}: Loss = {loss.item()}')

# # Resultados
# print(f'Weight: {model.weight.data.item()}, Bias: {model.bias.data.item()}')

# # Visualización (expansión)
# plt.plot(losses)
# plt.title('Curva de Pérdida')
# plt.xlabel('Épocas')
# plt.ylabel('MSE')
# plt.show()

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Datos sintéticos
np.random.seed(42)
X = np.arange(0, 10).reshape(-1, 1)
y = 2 * X.ravel() + 1 + np.random.randn(10) * 0.5

# Split (buena práctica para evaluación)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline: Escalado + Regresión Lineal
pipe = Pipeline([
    ('scaler', StandardScaler()),  # Normaliza features
    ('reg', LinearRegression())   # Modelo
])

# Entrenamiento y predicción
pipe.fit(X_train, y_train)
preds = pipe.predict(X_test)

# Evaluación
mse = mean_squared_error(y_test, preds)
print(f'MSE: {mse}')
print(f'Coeficientes: {pipe.named_steps["reg"].coef_[0]}, Intercepto: {pipe.named_steps["reg"].intercept_}')