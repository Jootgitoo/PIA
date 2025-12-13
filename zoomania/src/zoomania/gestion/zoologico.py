import json
import os
from zoomania.entidades.animal import Animal
from zoomania.entidades.cuidador import Cuidador
from zoomania.entidades.habitat import Habitat
from zoomania.utilidades.excepciones import HabitatLlenoError, AnimalNoEncontradoError, HabitatNoEncontradoError

BBDD_FILE = "datos_zoologico.json"

class Zoologico:
    def __init__(self):
        self.animales = []
        self.habitats = []
        self.cuidadores = []
        self.cargar_datos()

    def agregar_habitat(self, nombre, tipo, capacidad):
        nuevo_habitat = Habitat(nombre, tipo, capacidad)
        self.habitats.append(nuevo_habitat)
        self.guardar_datos()

    def eliminar_habitat(self, nombre_habitat):
        for i, habitat in enumerate(self.habitats):
            if habitat.nombre == nombre_habitat:
                del self.habitats[i]

                for animal in self.animales:
                    if animal.habitat_asignado == nombre_habitat:
                        animal.habitat_asignado = None
                self.guardar_datos()
                return True
        raise HabitatNoEncontradoError(nombre_habitat)

    def agregar_animal(self, nombre, especie, edad, nivel_hambre=0, habitat_nombre=None):
        nuevo_animal = Animal(nombre, especie, edad, nivel_hambre)
        self.animales.append(nuevo_animal)
        
        if habitat_nombre:
            self.asignar_animal_habitat(nombre, habitat_nombre)
        
        self.guardar_datos()

    def eliminar_animal(self, nombre_animal):
        for i, animal in enumerate(self.animales):
            if animal.nombre == nombre_animal:

                if animal.habitat_asignado:
                    habitat = self.buscar_habitat(animal.habitat_asignado)
                    if habitat:
                        habitat.eliminar_animal(nombre_animal)
                
                del self.animales[i]
                self.guardar_datos()
                return True
        raise AnimalNoEncontradoError(nombre_animal)

    def asignar_animal_habitat(self, nombre_animal, nombre_habitat):
        animal = self.buscar_animal(nombre_animal)
        habitat = self.buscar_habitat(nombre_habitat)

        if not animal:
            raise AnimalNoEncontradoError(nombre_animal)
        if not habitat:
            raise HabitatNoEncontradoError(nombre_habitat)

        if animal.habitat_asignado:
            habitat_actual = self.buscar_habitat(animal.habitat_asignado)
            if habitat_actual:
                habitat_actual.eliminar_animal(nombre_animal)

        habitat.agregar_animal(animal) 
        self.guardar_datos()

    def alimentar_animal(self, nombre_animal):
        animal = self.buscar_animal(nombre_animal)
        if not animal:
            raise AnimalNoEncontradoError(nombre_animal)
        
        animal.alimentar(20) 
        self.guardar_datos()

    def agregar_cuidador(self, nombre, turno):
        nuevo_cuidador = Cuidador(nombre, turno)
        self.cuidadores.append(nuevo_cuidador)
        self.guardar_datos()
        
    def asignar_cuidado(self, nombre_cuidador, nombre_animal):
        for cuidador in self.cuidadores:
            if cuidador.nombre == nombre_cuidador:
                cuidador.asignar_animal(nombre_animal)
                self.guardar_datos()
                return
        

    def buscar_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                return animal
        return None

    def buscar_habitat(self, nombre):
        for habitat in self.habitats:
            if habitat.nombre == nombre:
                return habitat
        return None

    def generar_informe(self):
        informe = "--- Informe del Zoológico ---\n"
        informe += f"Total Animales: {len(self.animales)}\n"
        informe += f"Total Hábitats: {len(self.habitats)}\n"
        informe += "Detalle Hábitats:\n"
        for h in self.habitats:
            informe += f"  - {h}\n"
            for a in h.animales_residentes:
                informe += f"    * {a}\n"
        return informe

    def guardar_datos(self):
        data = {
            "animales": [a.to_dict() for a in self.animales],
            "habitats": [h.to_dict() for h in self.habitats],
            "cuidadores": [c.to_dict() for c in self.cuidadores]
        }
        with open(BBDD_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def cargar_datos(self):
        if not os.path.exists(BBDD_FILE):
            return

        try:
            with open(BBDD_FILE, "r") as f:
                data = json.load(f)
                
            # Cargar hábitats primero
            self.habitats = [Habitat.from_dict(h) for h in data.get("habitats", [])]
            
            # Cargar animales
            self.animales = [Animal.from_dict(a) for a in data.get("animales", [])]
            
            # Cargar cuidadores
            self.cuidadores = [Cuidador.from_dict(c) for c in data.get("cuidadores", [])]
            
            for animal in self.animales:
                if animal.habitat_asignado:
                    habitat = self.buscar_habitat(animal.habitat_asignado)
                    if habitat:
                        habitat._animales_residentes.append(animal)
                        
        except (json.JSONDecodeError, KeyError):
            print("Error al cargar datos: Archivo corrupto o formato incorrecto.")