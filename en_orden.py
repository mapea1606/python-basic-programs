lista = [['a'], [['b'], 'c']]

lista2 = []

def en_orden(lista, ordenada):
    ordenada.append(lista)
    if type(lista[0]) == list:
        ordenada.append(lista[0])
        return ordenada
    else:
        ordenada = []
        return en_orden(lista[1:], ordenada)


ordenada = []
en_orden(lista, ordenada)
print(ordenada)
#for x in ordenada:
#    print(x)
