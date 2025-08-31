class Envio:
    def __init__(self, emisor, receptor):
        self.emisor = emisor
        self.receptor = receptor

    def enviar(self):
        pass

class Carta(Envio):
    def __init__(self, emisor, receptor):
        super().__init__(emisor, receptor)
        self.tiene_estampilla = False

    def poner_estampilla(self):
        self.tiene_estampilla = True

    def enviar(self):
        if self.tiene_estampilla:
            super().enviar()
            return True
        else:
            return False
