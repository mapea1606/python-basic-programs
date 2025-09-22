class Alcancia:
    def __init__(self, nombre, dinero, alcancia):
        self.nombre = nombre
        self.dinero = dinero
        self.siguiente_alcancia = alcancia

def sacar_dinero(alcancia, monto):
    nuevo_monto = alcancia.dinero - monto
    if alcancia.dinero >= monto:
        alcancia.dinero = nuevo_monto
        print(f"{alcancia.nombre}:{alcancia.dinero}")
        return (alcancia.nombre, alcancia.dinero)
    alcancia.dinero = 0
    print(f"{alcancia.nombre}:{alcancia.dinero}")
    return sacar_dinero(alcancia.siguiente_alcancia, abs(nuevo_monto))

a1 = Alcancia("Alcancia a1", 10000, None)
a2 = Alcancia("Alcancia a2", 700, a1)
a3 = Alcancia("Alcancia a3", 100, a2)
a4 = Alcancia("Alcancia a4", 500, a3)
a5 = Alcancia("Alcancia a5", 900, a4)
a6 = Alcancia("Alcancia a6", 800, a5)

print(sacar_dinero(a6, 5900))
