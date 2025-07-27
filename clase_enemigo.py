class Enemigo:
    def __init__(self, nombre, vida, fuerza_ataque):
        self.nombre = nombre
        self.vida = vida
        self.fuerza_ataque = fuerza_ataque

    def recibir_ataque(self, daño):
        if vida <= daño:
            vida = 0
        else:
            vida = vida - daño

    def atacar(self, otro):
        otro.recibir_ataque(fuerza_ataque)

    def __str__(self):
        txt = self.nombre + " - " + str(self.vida)
        return txt

a = Enemigo("Esqueleto", 8, 6)
b = Enemigo("Zombie", 10, 5)
print(a)
print(b)

a.recibir_ataque(5)
print(a)

a.atacar(b)
print(b)

a.atacar(b)
print(b)
        

