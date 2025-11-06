class Habitat:
    
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.lista_animales_residentes = [] 
        
        
    def agregar_animal(self, animal):
        if len(self.lista_animales_residentes) < self.capacidad:
            self.lista_animales_residentes.append(animal)
            return "Animal agregado correctamente"
        else:
            return "No se pudo añadir al hábitat"
        
        
    @nombre.deleter
    def nombre(self):
        del self.nombre
        
    @tipo.deleter
    def tipo(self):
        del self.tipo
        
    @capacidad.deleter
    def capacidad(self):
        del self.capacidad
        
    @lista_animales_residentes.deleter
    def lista_animales_residentes(self):
        del self.lista_animales_residentes
        
    