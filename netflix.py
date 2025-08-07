class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password

class Netflix:
    def __init__(self):
        self.usuarios = dict()
        self.siguiente_id = 0

    def conectarse(self, nombre, password):
        for usuarios in self.usuarios:
            usuario = self.usuarios[usuarios]
            if usuario.nombre == nombre and usuario.password == password:
                return True
            return False

    def agregar_usuario(self, usuario):
        self.usuarios[siguiente_id] = usuario
        self.siguiente_id += 1
