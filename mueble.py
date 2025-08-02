class Mueble:
    def __init__(self, h, a, l, v):
        self.alto = h
        self.ancho = a
        self.largo = l
        self.valor = v

    def precio(self):
        return self.alto * self.ancho * self.largo * self.valor


M1 = Mueble(1.0, 2.0, 3.0, 50)
M2 = Mueble(2.0, 2.0, 2.0, 600)
M3 = Mueble(1.5, 1.5, 3.0, 40)

tienda = [M1, M2, M3]

for mueble in tienda:
    print(mueble.precio())

tienda_aux = []
while len(tienda) > 0:
        menor = tienda[0]
        for mueble in tienda:
            if menor.precio() > mueble.precio():
                menor = mueble
        tienda.remove(menor)
        tienda_aux.append(menor)
tienda = tienda_aux

for mueble in tienda:
    print(mueble.precio())

