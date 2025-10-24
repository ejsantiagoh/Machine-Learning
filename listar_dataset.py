from sklearn import datasets

# Visualiza toda la documentación
# import sklearn.datasets
# help(sklearn.datasets)

# Ver todos los datasets disponibles
# print("Datasets incluidos en scikit-learn:")
# print([attr for attr in dir(datasets) if not attr.startswith('_') and 'load' in attr or 'fetch' in attr])

# ------------------------------------------------------
# Principales datasets de clasificación
# Dataset Iris (el que usaste)
iris = datasets.load_iris()
print("Iris - Forma:", iris.data.shape)  # (150, 4)

# Dataset Digits (dígitos escritos a mano)
digits = datasets.load_digits()
print("Digits - Forma:", digits.data.shape)  # (1797, 64)

# Dataset Wine (análisis de vinos)
wine = datasets.load_wine()
print("Wine - Forma:", wine.data.shape)  # (178, 13)

# Dataset Breast Cancer
cancer = datasets.load_breast_cancer()
print("Breast Cancer - Forma:", cancer.data.shape)  # (569, 30)

