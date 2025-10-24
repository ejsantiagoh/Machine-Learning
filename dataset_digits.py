from sklearn import datasets
import matplotlib.pyplot as plt

# Cargar dígitos escritos a mano
digits = datasets.load_digits()

print("Forma de los datos:", digits.data.shape)
print("Forma de las imágenes:", digits.images.shape)

# Visualizar algunas imágenes
fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='binary')
    ax.set_title(f'Dígito: {digits.target[i]}')
    ax.axis('off')
plt.show()