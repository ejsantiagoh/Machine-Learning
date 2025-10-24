import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score

df = pd.read_csv('train_house_prices.csv')

# features = ['MSSubClass', 'LotArea', 'OverallQual', 'YearBuilt', 'Neighborhood', 'GrLivArea']
# Features expandidas: agrega top importantes
features = [
    'MSSubClass', 'LotArea', 'OverallQual', 'YearBuilt', 'Neighborhood', 'GrLivArea',
    'TotalBsmtSF', 'GarageCars', 'GarageArea', 'FullBath', 'YearRemodAdd', 'BsmtFinSF1'
]
X = df[features]
y = df['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# numeric_features = ['LotArea', 'OverallQual', 'YearBuilt', 'GrLivArea']
# Actualiza numéricas y categóricas
numeric_features = [
    'LotArea', 'OverallQual', 'YearBuilt', 'GrLivArea',
    'TotalBsmtSF', 'GarageCars', 'GarageArea', 'FullBath', 'YearRemodAdd', 'BsmtFinSF1'
]
categorical_features = ['MSSubClass', 'Neighborhood']

numeric_transformer = Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())])
categorical_transformer = Pipeline([('imputer', SimpleImputer(strategy='constant')), ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer([('num', numeric_transformer, numeric_features), ('cat', categorical_transformer, categorical_features)])

# Usa XGBRegressor (parámetros default; puedes tunear como n_estimators=100, learning_rate=0.1, max_depth=3)
# pipe = Pipeline([('preprocessor', preprocessor), ('regressor', XGBRegressor(random_state=42))])

# XGBoost tuned: Params similares a tu GB para comparación
pipe = Pipeline([('preprocessor', preprocessor), ('regressor', XGBRegressor(
    n_estimators=300,      # Más árboles
    learning_rate=0.05,    # Baja para estabilidad
    max_depth=4,           # Moderada
    random_state=42,
    subsample=0.8,         # Extra para XGBoost: previene overfitting
    colsample_bytree=0.8,   # Muestreo de features
    reg_alpha=0.1,  # Nueva: regularización L1
    reg_lambda=1    # Nueva: regularización L2
))])

pipe.fit(X_train, y_train)
preds = pipe.predict(X_test)
mse = mean_squared_error(y_test, preds)
rmse = np.sqrt(mse)
mean_price = y_test.mean()
cv = (rmse / mean_price) * 100
r2 = r2_score(y_test, preds)

scores = cross_val_score(pipe, X, y, cv=5, scoring='neg_mean_squared_error')  # 5 folds
rmse_cv = np.sqrt(-scores.mean())

print(f'MSE: {mse}')
print(f'MSE: {mse:,.2f}')
print(f'RMSE: {rmse:,.2f}')
print(f'Precio promedio real: ${mean_price:,.2f}')
print(f'Error relativo (CV): {cv:.1f}%')
print(f'R²: {r2:.3f}')
print(f'RMSE promedio con CV: {rmse_cv:,.2f}')