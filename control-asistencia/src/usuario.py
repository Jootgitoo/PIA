class Usuario:
    
    def __init__(self, nombre, dni, foto):
        self.nombre = nombre
        self.dni = dni
        self.foto = foto

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "dni": self.dni,
            "foto": self.foto
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data.get("nombre"),
            dni=data.get("dni"),
            foto=data.get("foto")
        )
