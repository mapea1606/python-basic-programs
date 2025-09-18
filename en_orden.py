lista = [['a'], [['b'], 'c']]

lista2 = []

def en_orden(lista, ordenada):
    ordenada.append(lista)
    for elemento in lista: 
        if type(elemento) == list:
            en_orden(elemento, ordenada) 
    return ordenada

ordenada = []
en_orden(lista, ordenada)
print(ordenada)
for x in ordenada:
    print(x)
