class Cuidador:

    #Constructor
    def __init__(self, nombre, turno):
        self._nombre = nombre
        self._turno = turno
        self._animales_a_cargo = []

    #Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @property
    def turno(self):
        return self._turno
    
    @property
    def animales_a_cargo(self):
        return self._animales_a_cargo

    def asignar_animal(self, nombre_animal):
        if nombre_animal not in self._animales_a_cargo:
            self._animales_a_cargo.append(nombre_animal)

    def desasignar_animal(self, nombre_animal):
        if nombre_animal in self._animales_a_cargo:
            self._animales_a_cargo.remove(nombre_animal)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "turno": self.turno,
            "animales_a_cargo": self.animales_a_cargo
        }


    @classmethod
    def from_dict(cls, data):
        cuidador = cls(
            nombre=data["nombre"],
            turno=data["turno"]
        )
        cuidador._animales_a_cargo = data.get("animales_a_cargo", [])
        return cuidador

    def __str__(self):
        return f"{self.nombre} ({self.turno}) - Animales: {len(self.animales_a_cargo)}"