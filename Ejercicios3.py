class Personaje:
    def __init__(self, nombre, fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} fuerza: {self.fuerza}, velocidad: {self.velocidad}"
    
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**2)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**2)
        return Personaje(nuevo_nombre, nueva_fuerza,nueva_velocidad)
        
    
goku = Personaje("Goku",100,100)
vegeta = Personaje("vegeta",99,100)
gogeta = goku + vegeta
print(gogeta)