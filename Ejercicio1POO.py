class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("Estudiando...")
    
# pedro = Estudiante("Pedro",27,5)
# print(f"El nombre es: {pedro.nombre}, su edad es:{pedro.edad} y el grado: {pedro.grado}")
# print(pedro.edad)
# print(pedro.grado)

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
grado = input("Ingrese su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE\n\n
      Nombre:{estudiante.nombre}\n
      Edad:{estudiante.edad}\n
      Grado: {estudiante.grado}
      """)
        