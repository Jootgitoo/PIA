from zoomania.utilidades.excepciones import HabitatLlenoError

class Habitat:

    #Constructor
    def __init__(self, nombre, tipo, capacidad):
        self._nombre = nombre
        self._tipo = tipo
        self._capacidad = capacidad
        self._animales_residentes = []  # Lista de objetos Animal

    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo

    @property
    def capacidad(self):
        return self._capacidad

    @property
    def animales_residentes(self):
        return self._animales_residentes

    def agregar_animal(self, animal):
        """Agrega un animal al hábitat si hay espacio."""
        if len(self._animales_residentes) >= self._capacidad:
            raise HabitatLlenoError(self.nombre, self.capacidad)
        
        self._animales_residentes.append(animal)
        animal.habitat_asignado = self.nombre

    def eliminar_animal(self, nombre_animal):
        """Elimina un animal del hábitat por nombre."""
        for i, animal in enumerate(self._animales_residentes):
            if animal.nombre == nombre_animal:
                del self._animales_residentes[i]
                animal.habitat_asignado = None
                return animal
        return None

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "capacidad": self.capacidad,
            "animales": [animal.to_dict() for animal in self._animales_residentes]
        }

    @classmethod
    def from_dict(cls, data):
        habitat = cls(
            nombre=data["nombre"],
            tipo=data["tipo"],
            capacidad=data["capacidad"]
        )
        
        return habitat

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Capacidad: {len(self._animales_residentes)}/{self.capacidad}"