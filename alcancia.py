class Alcancia:
    def __init__(self, nombre, dinero, alcancia):
        self.nombre = nombre
        self.dinero = dinero
        self.siguiente_alcancia = alcancia

def sacar_dinero(alcancia, monto):
    alcancia.dinero = alcancia.dinero - monto
    if alcancia.dinero >= 0:
        return (alcancia.nombre, alcancia.dinero)
    return sacar_dinero(alcancia.siguiente_alcancia, abs(alcancia.dinero))

a1 = Alcancia("Chanchito de greda", 900, None)
a2 = Alcancia("Debajo del Colchón", 100, a1)

print(sacar_dinero(a2, 2000))
