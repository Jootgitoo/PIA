class Animal():
    
    def __init__(self, nombre, especie, edad, nivel_hambre, habitat_asignado):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.nivel_hambre = nivel_hambre
        self.habitat_asignado = habitat_asignado
        
        
    def alimentar_animal(self, nivel_comida_consumido):
        self.nivel_hambre -= nivel_comida_consumido
        
        print("Se ha consumido la comida")
        print(f"Nivel de hambre actual: {self.nivel_hambre}")
        
        
    @nombre.deleter
    def nombre(self):
        del self.nombre
        
    @especie.deleter
    def especie(self):
        del self.especie
        
    @edad.deleter
    def edad(self):
        del self.edad
        
    @nivel_hambre.deleter
    def nivel_hambre(self):
        del self.nivel_hambre
        
    @habitat_asignado.deleter
    def habitat_asignado(self):
        del self.habitat_asignado
        
    