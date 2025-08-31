class Paquete(Envio):
    def __init__(self, emisor, receptor, max_volumen):
        super().__init__(emisor, receptor)
        self.max_volumen = max_volumen
        self.esta_cerrado = False
        self.volumen_actual = 0
        self.peso_actual = 0

    def agregar_producto(self, peso, volumen):
        if self.esta_cerrado:
            self.esta_cerrado = False
        self.volumen_actual += volumen
        self.peso_actual += peso

    def cerrar(self):
        if self.volumen_actual <= self.max_volumen:
            self.esta_cerrado = True

    def enviar(self):
        if self.esta_cerrado and self.peso_actual <= 30:
            super().enviar()
            return True
        else:
            return False
