lista = [['a'], [['b'], 'c']]

lista2 = []

def en_orden(lista, ordenada):

    ordenada.append(lista)
    return ordenada

ordenada = []
en_orden(lista, ordenada)
print(ordenada)
#for x in ordenada:
#    print(x)
