class Vehiculo:
    def __init__(self, r):
        self.ruedas = r
        self.kilometraje = 0

    def avanzar(self):
        self.kilometraje += 10

    def tiempo_reparacion(self):
        if self.ruedas == 2:
            return 5
        if self.ruedas > 4:
            return 20
        return 10

from collections import deque

class Taller:
    def __init__(self):
        self.rapidos = deque()
        self.lentos = deque()

    def agregar_vehiculo(self, veh):
        if veh.tiempo_reparacion() < 15:
            self.rapidos.append(veh)
        else:
            self.lentos.append(veh)

    def siguiente_vehiculo(self):
        if len(self.rapidos) > 0:
            return self.rapidos.popleft()
        return self.lentos.popleft()

bici = Vehiculo(2)
auto = Vehiculo(4)
autobus = Vehiculo(6)
camion = Vehiculo(14)
triciclo = Vehiculo(3)

A = Taller()
A.agregar_vehiculo(bici)
A.agregar_vehiculo(auto)
A.agregar_vehiculo(autobus)
A.agregar_vehiculo(camion)
A.agregar_vehiculo(triciclo)

orden = []
for i in range(0,5):
    orden.append(A.siguiente_vehiculo())

for elemento in orden:
    print(elemento.ruedas)
