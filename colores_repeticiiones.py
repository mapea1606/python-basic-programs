def color_repeticion(lista):
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

    mas_repetidos = list()
    ultimo = lista_dos.pop()
    mas_repetidos.append(ultimo)
    j = 0
    print("***********")
    print(ultimo)
    print(mas_repetidos)

    while mayor_frecuencia == mas_repetidos[j][0]:            
        penultimo = lista_dos.pop()
        print(penultimo)
        print(penultimo[0])
        if mayor_frecuencia != penultimo[0]:
            break
        mas_repetidos.append(penultimo)
        print(mas_repetidos)    
       
        j += 1
     
    print("---------------------------------------")
    print(mas_repetidos)       
    print(len(mas_repetidos))
    print(mas_repetidos[0])
            
    for color_l in mas_repetidos:
        if color_l[1] == "azul":
            print(color_l)
            return (color_l[0], color_l[1])

    for color_l in mas_repetidos:
        if color_l[1] == "rojo":
            print(color_l)
            return (color_l[0], color_l[1])

    for color_l in mas_repetidos:
        if color_l[1] == "verde":
            print(color_l)
            return (color_l[0], color_l[1])

    for color_l in mas_repetidos:
        if color_l[1] == "amarillo":
            print(color_l)
            return (color_l[0], color_l[1])

colores = ["amarillo", "amarillo", "rojo", "amarillo", "verde", "verde", 
            "verde", "rojo", "rojo", "amarillo"]

(repeticion, col) = color_repeticion(colores)
print("El", col, "se repite", repeticion, "veces.")
