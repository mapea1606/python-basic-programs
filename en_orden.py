lista = [['a'], [['b'], 'c']]

lista2 = []

def en_orden(lista, ordenada):
    ordenada.append(lista)
    if len(lista) == 1 and type(lista) == list:
        ordenada.append(lista[0])
        return ordenada
    return en_orden(lista[0], ordenada)

ordenada = []
en_orden(lista, ordenada)
for x in ordenada:
    print(x)
