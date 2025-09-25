def sucesion(componente):
    sucesion = list()
    i = 0
    while i <= componente:
        sucesion.append(i)
        i += 1
    return sucesion

def tripletas(x, y, z):
    tripletas = list()
    for i in X:
        for j in Y:
            for k in Z:
                tripletas.append([i,j,k])
    return tripletas
 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    X = sucesion(x) 
    Y = sucesion(y)
    Z = sucesion(z)

    T = tripletas(X, Y, Z)

    nueva_T = list()

    for elem in T:
        if sum(elem) != n:
            nueva_T.append(elem)
    
    print(nueva_T)

