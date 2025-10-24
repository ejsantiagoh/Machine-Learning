class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Holaaaa...")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,universidad,notas):
        super().__init__(nombre,edad,nacionalidad)
        self.universidad = universidad
        self.notas = notas
        
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    # def mostrar_habilidad(self):
    #     return super().mostrar_habilidad()
    
    def presentarse(self):
        print( f"Hola soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")
    
brayan = EmpleadoArtista("Brayan", 20,"colombiano", "tekondo",20000, "campus")
# print()
brayan.presentarse()
# empleado1 = Empleado("Carlos",24,"colombiano","analista",4300000)

# estudiante1 = Estudiante("Jesus", 44,"Chileno","santiagode chile",70)
# print(empleado1.nombre)
# empleado1.hablar()


        