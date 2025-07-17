numero = int(input("Ingrese un numero: "))

primo = True


if numero == 1:
    primo = False
else:
    contador = 2

    while contador < numero:
        if numero % contador == 0:
            print(contador)
            primo = False
            break

        contador = contador + 1

print("El numero ", numero, " es primo: ", primo) 
