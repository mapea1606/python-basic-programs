class Mascota:
    def __init__(self, n, h):
        self.nombre = n
        self.dueño = h

    def saludar(self, humano):
        if humano == self.dueño:
            return 'Hola '+ humano.nombre
        return 'grrr, no te conozco ' + humano.nombre

class Humano:
    def __init__(self, n):
        self.nombre = n

humano = Humano('Alex')
perro = Mascota('Rex' , humano)
humano2 = Humano("Pancho")

print(perro.saludar(humano))
print(perro.saludar(humano2))
