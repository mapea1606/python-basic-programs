lista = [['a'], [['b'], 'c']]

lista2 = []

def en_orden(lista, ordenada):
    ordenada.append(lista)
    if type(lista) == list:
        primero = lista[0]
        resto = lista[1:]
        ordenada.append(primero)
        return ordenada
    return primero + en_orden(resto, ordenada)


ordenada = []
en_orden(lista, ordenada)
print(ordenada)
for x in ordenada:
    print(x)
