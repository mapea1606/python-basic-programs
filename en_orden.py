lista = [['a'], [['b'], 'c']]

lista2 = []

def en_orden(lista, ordenada):
    ordenada.append(lista)
    if type(lista) == list:
        resto = lista[1:]
        ordenada.append(primero)
        return ordenada
    plana = primero +  en_orden(resto, ordenada)
    return plana

ordenada = []
en_orden(lista, ordenada)
print(ordenada)
for x in ordenada:
    print(x)
