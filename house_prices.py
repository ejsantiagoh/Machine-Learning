import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

df = pd.read_csv('train_house_prices.csv')


# print("Columnas disponibles:")
# print(df.columns.tolist())
# print(f"\nPrimeras filas:")
# print(df.head())

features = ['MSSubClass','LotArea','OverallQual','YearBuilt','Neighborhood', 'GrLivArea']
X = df[features]
y = df['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

numeric_features =['LotArea','OverallQual','YearBuilt','GrLivArea']
categorical_features = ['MSSubClass','Neighborhood']

numeric_transformer = Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())])
categorical_transformer = Pipeline([('imputer', SimpleImputer(strategy='constant')),('onehot',OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer([('num',numeric_transformer, numeric_features),('cat', categorical_transformer, categorical_features)])

# pipe = Pipeline([('preprocessor', preprocessor),('regressor',GradientBoostingRegressor())])
# pipe.fit(X_train,y_train)
# preds = pipe.predict(X_test)

# Pipeline con Gradient Boosting
pipe_gb = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(
        n_estimators=300,     # Más árboles = mejor, pero más lento
        learning_rate=0.05,   # Tasa de aprendizaje baja para estabilidad
        max_depth=4,          # Profundidad moderada
        random_state=42
    ))
])
pipe_gb.fit(X_train, y_train)
preds = pipe_gb.predict(X_test)

mse = mean_squared_error(y_test, preds)
rmse = np.sqrt(mse)
mean_price = y_test.mean()
cv = (rmse / mean_price) * 100
r2 = r2_score(y_test, preds)    # cuánto explica el modelo


print(f'MSE: {mse}')
print(f'MSE: {mse:,.2f}')
print(f'RMSE: {rmse:,.2f}')
print(f'Precio promedio real: ${mean_price:,.2f}')
print(f'Error relativo (CV): {cv:.1f}%')
print(f'R²: {r2:.3f}')  # >0.85 es bueno