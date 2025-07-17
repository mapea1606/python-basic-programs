def panprimo(n):
    def es_pandigital(n):
        i = 0
        while(i < 10):
            letra = str(i)
            if letra in n:
                i += 1
            else:
                return False
        return True
    
    if(es_pandigital(n)):
        print("El numero es pandigital")
    else:
        print("El numero no es pandigital")

    def obtener_resto(n):
        return int(n) % 1000

    resto = obtener_resto(n)
    print("El resto de tres cifras es: ", resto)

    def es_primo(resto):
        i = 2
        while(resto != i):
            if(resto % i == 0):
                print(i)
                return False
            i += 1
        return True

    if(es_primo(resto)):
        print("El numero es primo")
    else:
        print("El numero no es primo")

    if(es_primo(resto) and es_pandigital(n)):
        return True
    else:
        return False

numero = input("Ingresar un numero de más de diez digitos: ")

if(panprimo(numero)):
    print("El número es panprimo")
else:
    print("El numero no es panprimo")

