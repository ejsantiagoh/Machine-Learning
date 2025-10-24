class Auto():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "Encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
    
miauto = Auto()
miauto.conducir()