texto = input("Ingrese una lista: ")
print("Primero:", texto[0])
print("No Lista:", texto)
no_olvidar = []
inicio = 0
for i in range(0,len(texto)):
    if texto[i] == ",":
        no_olvidar.append(texto[inicio:i])
        inicio = i + 1
no_olvidar.append(texto[inicio:])
print("Lista:", no_olvidar)
