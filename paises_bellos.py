paises = [[0, "España", "Madrid"],
          [2, "Alemania", "Berlin"],
          [1, "Francia", "Paris"],
          [3, "Italia", "Roma"]]

belleza = [[2, 0.57],
           [1, 0.81],
           [3, 0.68],
           [0, 0.62]]

#print(paises)
#print(belleza)

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

