#Programa que arroja una lista de tuplas de dos entradas
#con los países más bellos en orden descendente.
#La función trabaja a partir de dos listas bidimensionales dadas.

paises = [[0, "España", "Madrid"],    #Lista de países con un id
          [2, "Alemania", "Berlin"],  #el país y su capital
          [1, "Francia", "Paris"],
          [3, "Italia", "Roma"]]

belleza = [[2, 0.57],                 #Lista con el id que identifica
           [1, 0.81],                 #a cada país y su indice de belleza
           [3, 0.68],
           [0, 0.62]]

def paises_bellos(paises, belleza):
    pais_bello = []
    belleza.sort(key=lambda elem: elem[0])
    paises.sort(key=lambda elem: elem[0])
    for i in range(len(belleza)):
        p = (paises[i][1], belleza[i][1])
        pais_bello.append(p)
    pais_bello.sort(key=lambda elem: elem[1], reverse=True)
    
    return pais_bello

print(paises_bellos(paises, belleza))

