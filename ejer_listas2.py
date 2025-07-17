estudiantes = ["Mario Avedaño",
               "Policarpo Avedaño",
               "Juan Bodoque",
               "Juanin Harry",
               "Mario Hugo",
               "Dylan Manguera",
               "Eusebio Manguera"]

# def agregar_estudiante(lista, estudiante):
#     lista.append(estudiante)
#     apellidos = list()
#     for elem in lista:
#         apellido = ""
#         for i in len(elem):
#             apellido = apellido + elem[i] 
# 
#     print(lista)
# 
#agregar_estudiante(estudiantes, "Eliza Manguera")

estudiante = "Eliza Manguera"
nombre = []

for i in range(len(estudiante)):
    if estudiante[i] == " ":
        esp_vacio = i

nom = estudiante[0:esp_vacio]
ap = estudiante[esp_vacio+1:len(estudiante)]

nombre = [estudiante, nom, ap]

def enlistar(lista):
    nombres = []
    vacios = []
    j = 0
    for elem in lista:
        for i in range(len(elem)):
            if elem[i] == " ":
                vacios.append(i)
        print(elem)
        print(vacios)


enlistar(estudiantes)

#print(nom)
#print(ap)
#print(nombre)
#print(esp_vacio)


