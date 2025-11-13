class Habitat:
    
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.lista_animales_residentes = [] 
        
    def __init__():
        pass
        
    def agregar_animal(self, animal):
        if len(self.lista_animales_residentes) < self.capacidad:
            self.lista_animales_residentes.append(animal)
            return "Animal agregado correctamente"
        else:
            return "No se pudo añadir al hábitat"
        
        

        
    