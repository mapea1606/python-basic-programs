class PaqueteMejorado(Paquete):
    def __init__(self, emisor, receptor, max_volumen):
        super().__init__(emisor, receptor, max_volumen)
        self.ya_enviado = False
    
    def enviar(self):
        if self.emisor == self.receptor:
            return False
        if self.ya_enviado:
            return False
        if super().enviar():
            self.ya_enviado = True
            return True
        else:
            return False
