#Ejercicio 7

def ganador(votos):
    mayor = votos[0]
    for cand in votos:
        if cand[1] > mayor[1]:
            mayor = cand
    return mayor[0]

resultados = [["Alfredo",20], ["Marcela",40], ["Ignacio",30], ["Loreto",10]]

mayoria = ganador(resultados)
print(mayoria)

#Ejercicio 8

tablero = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(3):
    for j in range(3):
        print(tablero[j][i], end=" ")

print("\n")

for i in range(9):
    print(tablero[i%3][i//3], end=" ")

print("\n")

print(1//3) #0
print(1%3) #1
print(tablero[2%3][2//3]) #tablero[2][0]
