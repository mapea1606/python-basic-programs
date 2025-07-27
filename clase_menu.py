class Menu:
    def __init__(self, comidas, precios):
        self.comidas = comidas
        self.precios = precios

    def __str__(self):
        i = 0
        txt = ""
        for i in range(len(self.comidas)):
            if i < len(self.comidas)-1:
                txt = txt + self.comidas[i] + ": " + str(self.precios[i]) + "\n"
            elif i == len(comidas)-1:
                txt = txt + self.comidas[i] + ": " + str(self.precios[i])
        return txt

comidas = ["Pato a la mostaza", "Hamburguesa", "Ensalada", "Lasagna"]
precios = [20000, 8000, 6000, 9000]
menu = Menu(comidas, precios)

print(menu)
