def calculo(numero):
    resultado = (numero - 3) ** 3
    return resultado

print(calculo(8))
salida = calculo(5)
print(salida + 100)

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(8))
print(es_par(9))
