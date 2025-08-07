class A:
    def __init__(self, val):
        self.value = val

    def sumar_a_valor(self, suma):
        self.value += suma

    def sumar_valor_y_retornar(self, suma):
        self.sumar_a_valor(suma)
        return self.value

class B(A):
    def __init__(self, val):
        self.value = val + 2

    def sumar_valor_y_retornar(self, suma):
        self.sumar_a_valor(suma)
        return self.value

foo = B(10)
print(foo.sumar_valor_y_retornar(5))
