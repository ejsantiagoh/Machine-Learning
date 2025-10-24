class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())

hacer_sonido(perro )