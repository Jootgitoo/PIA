class Animal:
    
    #Constructor
    def __init__(self, nombre, especie, edad, nivel_hambre=0, habitat_asignado=None):
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        self._nivel_hambre = nivel_hambre
        self._habitat_asignado = habitat_asignado

    #Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @property
    def especie(self):
        return self._especie

    @property
    def edad(self):
        return self._edad

    @property
    def nivel_hambre(self):
        return self._nivel_hambre

    @nivel_hambre.setter
    def nivel_hambre(self, valor):
        if valor < 0:
            self._nivel_hambre = 0
        elif valor > 100:
            self._nivel_hambre = 100
        else:
            self._nivel_hambre = valor

    @property
    def habitat_asignado(self):
        return self._habitat_asignado

    @habitat_asignado.setter
    def habitat_asignado(self, habitat):
        self._habitat_asignado = habitat

    def alimentar(self, cantidad):
        """Reduce el nivel de hambre del animal."""
        self.nivel_hambre -= cantidad

    def to_dict(self):
        """Convierte la instancia a un diccionario para serialización."""
        return {
            "nombre": self.nombre,
            "especie": self.especie,
            "edad": self.edad,
            "nivel_hambre": self.nivel_hambre,
            "habitat_asignado": self.habitat_asignado
        }

    @classmethod
    def from_dict(cls, data):
        """Crea una instancia desde un diccionario."""
        return cls(
            nombre=data["nombre"],
            especie=data["especie"],
            edad=data["edad"],
            nivel_hambre=data["nivel_hambre"],
            habitat_asignado=data.get("habitat_asignado")
        )

    #toString de python
    def __str__(self):
        return f"{self.nombre} ({self.especie}) - Hambre: {self.nivel_hambre}%"