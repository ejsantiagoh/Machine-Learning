class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    
dalto = Persona("Lucas",21)
print(dalto)

lista = (1,2,3)

print(lista)