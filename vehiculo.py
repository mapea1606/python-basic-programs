class Vehiculo:
    
    def __init__(self):
        self.ruedas = 4
        self.kilometraje = 0
        
    def avanzar(self, km):
        self.kilometraje += km

    def cambiar_neumaticos(self):
        print('Se han cambiado las ' +self.ruedas+' ruedas')


class Camion(Vehiculo):
    def __init__(self):
        super().__init__()
        self.ruedas = 6

    def ver_kilometraje(self):
        return self.kilometraje
