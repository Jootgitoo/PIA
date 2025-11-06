class Cuidador:
    
    def __init__(self, nombre, turno, lista_animales_cuida):
        self.nombre = nombre
        self.turno = turno
        self.lista_animales_cuida = lista_animales_cuida
        
    
    @nombre.deleter
    def nombre(self):
        del self.nombre
        
    @turno.deleter
    def turno(self):
        del self.turno
    
    @lista_animales_cuida.deleter
    def lista_animales_cuida(self):
        del self.lista_animales_cuida