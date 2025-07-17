def mcd(a, b):
    if a > b:
        if a % b == 0:
            return b
        i = b - 1
        while i > 0:
            if (a % i == 0) and (b % i == 0):
                return i
            i -= 1
    elif a < b:
        if b % a == 0:
            return a
        i = a - 1
        while i > 0:
            if (a % i == 0) and (b % i == 0):
                return i
            i -= 1
    else:
        return a

num_1 = int(input("Introduzca un entero positivo: n1 = "))
num_2 = int(input("Introduzca un entero positivo: n2 = "))

print("mcd = ", mcd(num_1,num_2)) 


