class Cuidador:
    
    def __init__(self, nombre, turno, lista_animales_cuida):
        self.nombre = nombre
        self.turno = turno
        self.lista_animales_cuida = lista_animales_cuida
        
    @property
    def nombre(self):
        return self.nombre
    
    @nombre.deleter
    def nombre(self):
        del self.nombre
        
    @property
    def turno(self):
        return self.turno
    
    @turno.deleter
    def turno(self):
        del self.turno
    
    @property
    def lista_animales_cuida(self):
        return self.lista_animales_cuida
    
    @lista_animales_cuida.deleter
    def lista_animales_cuida(self):
        del self.lista_animales_cuida