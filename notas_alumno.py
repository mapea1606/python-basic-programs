lista1 = [["Nombre", "Numero alumno", "Correo", "Nota final"],
          ["Alicia", 16848, "amartinez@gmail.com", 5.7],
          ["Marco", 19845, "marenas@gmail.com", 4.8]]

lista2 = [["Numero alumno", "Nota final", "Nombre", "Color favorito"],
          [16848, 5.7, "Alicia", "Rojo"],
          [19845, 4.8, "Marco", "Verde"],
          [19515, 6.2, "Federico", "Azul"]]

#print(lista1)
#print(lista2)

def notas_alumnos(lista):
    nota = []
    for j in range(len(lista[0])):
        if lista[0][j] == "Nombre":
            i_nombre = j
        if lista[0][j] == "Nota final":
            i_nota = j
    for elem in lista[1:]:
        p = (elem[i_nombre], elem[i_nota])
        nota.append(p)
    return nota

print(notas_alumnos(lista1))

