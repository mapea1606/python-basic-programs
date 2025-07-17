lista = [1,4,6,2,4,3,1,1,3,5,6,7,3,4,5,5,5,3,3,2,1,2,1,1,1,2,6,6]

print(lista)

def max_repetido(lista):
    lista.sort()
    contador = 0
    repeticiones = []
    aux = lista[0]
    for i in range(len(lista)):
        if aux == lista[i]:
            contador += 1
            if i == len(lista)-1:
                repeticiones.append(contador)
        elif aux != lista[i]:
            repeticiones.append(contador)
            contador = 1
            aux = lista[i]
            if i == len(lista)-1:
                repeticiones.append(contador)
    return max(repeticiones) 

print(max_repetido(lista))


