lista = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4]

def imprimir(lista, pos):
    if pos < len(lista):
        print(lista[pos])
        imprimir(lista, pos+1)

imprimir(lista, 0)
