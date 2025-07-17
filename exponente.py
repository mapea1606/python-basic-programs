def exponente(n):
    exp = 0
    prod = 1
    while prod <= n:
        prod *= 2
        exp += 1
    if n % prod == 0:
        return exp
    else:
        return exp - 1

numero = int(input("Ingrese un número entero: "))

print("El exponente de la potencia de dos menor o igual es: ", exponente(numero))
