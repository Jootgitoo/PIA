class Zoologico:
    
    def __init__(self, lista_animales, lista_habitats, lista_cuidadores):
        self.lista_animales = lista_animales
        self.lista_habitats = lista_habitats
        self.lista_cuidadores = lista_cuidadores
        
        
    def mostrar_informacion_zoologico(self):
        print("----- Información del Zoológico -----")
        print(f"Número de animales: {self.lista_animales}")
        print(f"Número de hábitats: {self.lista_habitats}")
        print(f"Número de cuidadores: {self.lista_cuidadores}")
        print("-------------------------------------")
        
    def guardar_datos(self):
        archivo = open("datos_zoologico.txt", "w")
        archivo.write("Datos del Zoológico\n")
        archivo.write(f"-------------------------------------------\n")
        archivo.write(f"Animales: {self.lista_animales}\n")
        archivo.write(f"-------------------------------------------\n")
        archivo.write(f"Habitats: {self.lista_habitats}\n")
        archivo.write(f"-------------------------------------------\n")
        archivo.write(f"Cuidadores: {self.lista_cuidadores}\n")
        archivo.write(f"-------------------------------------------\n")
        archivo.close()
        
        #PUNTO 4