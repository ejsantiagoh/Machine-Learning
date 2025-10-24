from abc import ABC, abstractmethod

class verificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario(verificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica para verificar palabras
        pass

class ServicioOnline(verificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica para verificar palabras desde el servicio web
        pass

class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador = verificador
        
    def corregir_texto(self,texto):
        # Usamos el verificador para corregir texto
        
corrector = CorrectorOrtografico(Diccionario())