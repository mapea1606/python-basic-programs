def color_frecuente(lista):
    lista_dos = list()

    ocurrencia = 0    
    for color in lista:
        if color == "azul":
            ocurrencia += 1
    rep = [ocurrencia, "azul"]      
    lista_dos.append(rep) 

    ocurrencia = 0
    for color in lista:
        if color == "rojo":
            ocurrencia += 1
    rep = [ocurrencia, "rojo"] 
    lista_dos.append(rep)

    ocurrencia = 0
    for color in lista:
        if color == "verde":
            ocurrencia += 1
    rep = [ocurrencia, "verde"] 
    lista_dos.append(rep)
    
    ocurrencia = 0
    for color in lista:
        if color == "amarillo":
            ocurrencia += 1
    rep = [ocurrencia, "amarillo"] 
    lista_dos.append(rep)

    lista_dos.sort()
    mayor_frecuencia = lista_dos[len(lista_dos)-1][0]
           
    for color_l in lista_dos:
        if color_l[0] == mayor_frecuencia and color_l[1] == "azul":
            return (color_l[1], color_l[0])

    for color_l in lista_dos:
        if color_l[0] == mayor_frecuencia and color_l[1] == "rojo":
            return (color_l[1], color_l[0])

    for color_l in lista_dos:
        if color_l[0] == mayor_frecuencia and color_l[1] == "verde":
            return (color_l[1], color_l[0])

    for color_l in lista_dos:
        if color_l[0] == mayor_frecuencia and color_l[1] == "amarillo":
            return (color_l[1], color_l[0])

colores = ["amarillo", "amarillo", "rojo", "amarillo", "verde", "verde", 
            "verde", "rojo", "rojo", "amarillo"]

(col, repet) = color_frecuente(colores)
print(col, repet)
