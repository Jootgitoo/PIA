class ZoomaniaError(Exception):
    """Clase base para excepciones en Zoomania."""
    pass

class HabitatLlenoError(ZoomaniaError):
    """Excepción lanzada cuando se intenta agregar un animal a un hábitat sin capacidad."""
    def __init__(self, nombre_habitat, capacidad):
        self.nombre_habitat = nombre_habitat
        self.capacidad = capacidad
        super().__init__(f"El hábitat '{nombre_habitat}' está lleno (Capacidad: {capacidad}).")

class AnimalNoEncontradoError(ZoomaniaError):
    """Excepción lanzada cuando no se encuentra un animal."""
    def __init__(self, nombre_animal):
        self.nombre_animal = nombre_animal
        super().__init__(f"El animal '{nombre_animal}' no fue encontrado.")

class HabitatNoEncontradoError(ZoomaniaError):
    """Excepción lanzada cuando no se encuentra un hábitat."""
    def __init__(self, nombre_habitat):
        self.nombre_habitat = nombre_habitat
        super().__init__(f"El hábitat '{nombre_habitat}' no fue encontrado.")
