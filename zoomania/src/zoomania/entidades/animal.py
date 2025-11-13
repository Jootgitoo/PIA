class Animal():
    
    def __init__(self, nombre, especie, edad, nivel_hambre, habitat_asignado):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.nivel_hambre = nivel_hambre
        self.habitat_asignado = habitat_asignado
        self.lista_animales = []
        
        
    def __init__(self):
        pass
        
    def alimentar_animal(self, nivel_comida_consumido):
        
        if self.nivel_hambre - nivel_comida_consumido < 0:
            raise ValueError("El nivel de comida consumido es mayor al nivel de hambre del animal")
        else: 
            self.nivel_hambre -= nivel_comida_consumido
        
        print("Se ha consumido la comida")
        print(f"Nivel de hambre actual: {self.nivel_hambre}")
        
    def agregar_a_lista(self, animal):
        self.lista_animales.append(animal)
            
        
    @property
    def nombre(self):
        return self.nombre   
        
    @nombre.deleter
    def nombre(self):
        del self.nombre
        
    @property
    def especie(self):
        return self.especie
    
    @especie.deleter
    def especie(self):
        del self.especie
       
    @property
    def edad(self):
        return self.edad
     
    @edad.deleter
    def edad(self):
        del self.edad
        
    @property
    def nivel_hambre(self):
        return self.nivel_hambre
    
    @nivel_hambre.deleter
    def nivel_hambre(self):
        del self.nivel_hambre
    
    @property
    def habitat_asignado(self):
        return self.habitat_asignado
        
    @habitat_asignado.deleter
    def habitat_asignado(self):
        del self.habitat_asignado
        
    @property
    def lista_animales(self):
        return self.lista_animales
    
    @lista_animales.deleter
    def lista_animales(self):
        del self.lista_animales