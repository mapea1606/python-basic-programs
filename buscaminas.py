def buscaminas(tablero, i, j):

    while i < 0 or i >= len(tablero) or j < 0 or j >= len(tablero[0]):
        print("ERROR. Coordenadas fuera del tablero.")
        i = int(input("Ingresa coordenadas validas: x = "))
        j = int(input("Ingresa coordenadas validas: y = "))

    bombas = 0

    if i == 0:
        for elem in tablero[i:i+2]:
            if j == 0:
                for subelem in elem[j:j+2]:
                    if subelem == "X":
                        bombas += 1
            elif j == len(tablero[0]) - 1:
                for subelem in elem[j-1:j+1]:
                    if subelem == "X":
                        bombas += 1
            else:
                for subelem in elem[j-1:j+2]:
                    if subelem == "X":
                        bombas += 1

    elif i == len(tablero) - 1:
        for elem in tablero[i-1:i+1]:
            if j == 0:
                for subelem in elem[j:j+2]:
                    if subelem == "X":
                        bombas += 1
            elif j == len(tablero[0]) - 1:
                for subelem in elem[j-1:j+1]:
                    if subelem == "X":
                        bombas += 1
            else:
                for subelem in elem[j-1:j+2]:
                    if subelem == "X":
                        bombas += 1

    else:
        for elem in tablero[i-1:i+2]:
            if j == 0:
                for subelem in elem[j:j+2]:
                    if subelem == "X":
                        bombas += 1
            elif j == len(tablero[0]) - 1:
                for subelem in elem[j-1:j+1]:
                    if subelem == "X":
                        bombas += 1
            else:
                for subelem in elem[j-1:j+2]:
                    if subelem == "X":
                        bombas += 1

    return bombas



tablero = [["X", " ", " ", "X", " ", " ", "X", " ", " ", " "], 
            [" ", " ", " ", "X", " ", "X", " ", " ", "X", " "], 
            [" ", " ", "X", " ", " ", " ", " ", " ", " ", " "], 
            [" ", " ", "X", " ", " ", " ", " ", "X", " ", " "],
            []
            []
            []
            []
            []
            []]

bombas = buscaminas(tablero, 10, 0)

print(len(tablero))
print(len(tablero[0]))
print(bombas)
