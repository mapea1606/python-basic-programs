def color_repeticion(lista):
    print(lista)
    lista_dos = list()
    for j in range(len(lista)):
        ocu = 0
        color = lista[j]
        for elem in lista:
            if elem == color:
                ocu += 1
                rep = [ocu, color]
       
        lista_dos.append(rep)    

    lista_dos.sort()
    print(lista_dos)
    mayor_frecuencia = lista_dos[len(lista_dos)-1][0]
           
    for color_l in lista_dos:
        if color_l[0] == mayor_frecuencia and color_l[1] == "azul":
            print(color_l)
            return (color_l[1], color_l[0])

    for color_l in lista_dos:
        if color_l[0] == mayor_frecuencia and color_l[1] == "rojo":
            print(color_l)
            return (color_l[1], color_l[0])

    for color_l in lista_dos:
        if color_l[0] == mayor_frecuencia and color_l[1] == "verde":
            print(color_l)
            return (color_l[1], color_l[0])

    for color_l in lista_dos:
        if color_l[0] == mayor_frecuencia and color_l[1] == "amarillo":
            print(color_l)
            return (color_l[1], color_l[0])

colores = ["amarillo", "amarillo", "rojo", "amarillo", "verde", "verde", 
            "verde", "rojo", "rojo", "amarillo"]

(col, repet) = color_repeticion(colores)
print(col, repet)
