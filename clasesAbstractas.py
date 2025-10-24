from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre,edad,sexo,trabajo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.trabajo = trabajo
    
    @abstractmethod
    def trabajar(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

class Programador(Persona):
    def __init__(self, nombre, edad, sexo, trabajo):
        super().__init__(nombre, edad, sexo, trabajo)
    
    def trabajar(self):
        print(f"{self.nombre} está programando como {self.trabajo}.")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, trabajo):
        super().__init__(nombre, edad, sexo, trabajo)
    
    def trabajar(self):
        print(f"Mi nombre es {self.nombre} y estoy estudiando {self.trabajo}.")
        
dalto = Programador("lucas", 12, "Masculino", "Junior")
dalto.trabajar()
dalto = Estudiante("lucas", 12, "Masculino", "Programacion")
dalto.trabajar()
# dalto.presentarse()