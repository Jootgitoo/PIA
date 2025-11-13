from zoomania.entidades import animal, cuidador, habitat

class Zoologico:
    
    def __init__(self, lista_animales, lista_habitats, lista_cuidadores):
        self.lista_animales = lista_animales
        self.lista_habitats = lista_habitats
        self.lista_cuidadores = lista_cuidadores
        
        
    def agrear_animal(self):
        nombre = input("Nombre del animal: ")
        especie = input("Especia del animal:")
        
        edad = int(input("Edad del animal: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        
        nivel_hambre = int(input("Nivel de hambre del animal:"))
        if nivel_hambre < 0 or nivel_hambre > 100:
            raise ValueError("El nivel de hambre debe estar entre 0 y 100.")
        

        habitat_aisgnado = input("Habitat asignado: ")
        
        for habitat in self.lista_habitats:
            if habitat.nombre == habitat_aisgnado.nombre:
                if len(habitat.lista_animales_residentes) >= habitat.capacidad:
                    raise ValueError("El hábitat no tiene capacidad disponible.")
                
                    
        
        #Crear el animal
        animal_usurario = animal(nombre, especie, edad, nivel_hambre, habitat_aisgnado)
        
        #Lo añado a la lista
        #a.agregar_a_lista(animal_usurario)
        
        
    #def eliminar_animal():
    
    #def agrear_cuidador():
    #def eliminar_cuidador():
    
    #def agrear_habitat():
    #def eliminar_habitat():
    
    #def asignar_animal_habitat():
        # Comprobar que el hábitat tiene capacidad disponible
            
    
        
    def mostrar_informacion_zoologico(self):
        print("----- Información del Zoológico -----")
        print(f"Número de animales: {self.lista_animales}")
        print(f"Número de hábitats: {self.lista_habitats}")
        print(f"Número de cuidadores: {self.lista_cuidadores}")
        print("-------------------------------------")
        
        
    def guardar_datos(self):
        archivo = open("datos_zoologico.txt", "w")
        archivo = open("src/zoomania/bbdd/datos_zoologico.txt", "w")
        archivo.write("Datos del Zoológico\n")
        archivo.write(f"-------------------------------------------\n")
        archivo.write(f"Animales: {self.lista_animales}\n")
        archivo.write(f"-------------------------------------------\n")
        archivo.write(f"Habitats: {self.lista_habitats}\n")
        archivo.write(f"-------------------------------------------\n")
        archivo.write(f"Cuidadores: {self.lista_cuidadores}\n")
        archivo.write(f"-------------------------------------------\n")
        archivo.close()
        
        