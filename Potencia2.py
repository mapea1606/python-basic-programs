def exponente(n):
    exp = 0

    while 2**exp <= n:
        exp += 1

        if 2**exp > n:
            return exp - 1

n = int(input("Enter an integer: "))

exp = exponente(n)

print("El exponente más próximo es: "+str(exp))

print(str(2**exp)+"=2**"+str(exp)+"<="+str(n))
