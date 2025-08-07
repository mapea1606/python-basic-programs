class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password

class Netflix:
    def __init__(self):
        self.usuarios = dict()
        self.siguiente_id = 0

    def agregar_usuario(self, usuario):
        self.usuarios[siguiente_id] = usuario
        self.siguiente_id += 1
