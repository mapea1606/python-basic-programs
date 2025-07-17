def max_repeticion(lista):
    print(lista)
    lista.sort()
    print(lista)
    frecuencia = []
    contador = 0
    for i in range(len(lista)):
        if i > 0 and lista[i] != lista[i-1]:
            print(lista[i-1], "cambio a", lista[i])
            print(contador)
            frecuencia.append(contador)
            contador = 0
        contador += 1
    frecuencia.sort()
    print(frecuencia)
    maxima = frecuencia.pop()
    return maxima

def popo

lista = [11,44,66,22,44,33,11,11,33,55,66,77,33,44,55,55,55,33,33,22,11,22,11,11,11,22,66,66,
         77,77,77,77,77,77,77,77,77,77,77,77,77]

max_repeticion(lista)
