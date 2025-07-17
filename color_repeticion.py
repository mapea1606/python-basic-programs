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
    print("---------------------------------------")
    print(mas_repetidos)
    print("---------------------------------------")

    while mayor_frecuencia == mas_repetidos[j][0]:            
           # if 
        penultimo = lista_dos.pop()
        print(penultimo)
        print(penultimo[1])
        print(mas_repetidos[j][1])
        if penultimo[0] == mas_repetidos[j][0]:
            mas_repetidos.append(penultimo)
            print(mas_repetidos)    
            print(mas_repetidos[j][1])
        j += 1
     
    print("---------------------------------------")
    print(mas_repetidos)       
    print(len(mas_repetidos))
    print(mas_repetidos[0])
            
colores = ["amarillo", "azul", "rojo", "azul", "verde", "verde", 
            "verde", "amarillo", "rojo", "azul"]

color_repeticion(colores)
