class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Llamando desde tu: {self.modelo}")
        
    def cortar(self):
        print(f"colgó la llamada desde tu: {self.modelo}")
        
celular1 = Celular("Xiaomi","Mi 14T", "50MP")

celular1.cortar()

        