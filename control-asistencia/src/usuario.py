class Usuario:
    
    def __init__(self, nombre, dni, foto):
        self.nombre = nombre
        self.dni = dni
        self.foto = foto

    def get_nombre(self):
        return self.nombre

    def get_dni(self):
        return self.dni

    def get_foto(self):
        return self.foto

    def get_user(self):
        return {
            "nombre": self.nombre,
            "dni": self.dni,
            "foto": self.foto
        }
