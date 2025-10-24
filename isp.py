from abc import ABC, abstractmethod
class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass

class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass

class Durmiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass
    


class Humano(Comedor, Trabajador, Durmiente):
    def comer(self):
        print("El humnao esta comiendo")
    
    def trabajar(self):
        print("El humano esta trabajando")
    
    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("El Robot esta trabajando")
        
robot = Robot()
humano = Humano()
robot.trabajar()
humano.trabajar()