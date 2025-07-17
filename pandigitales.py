def es_primo(numero):
    i = 2
    while i < numero:
        if numero % i == 0:
            return False
        i += 1
    return True

def contador_digitos(numero):
    i = 1
    digitos = 0
    while i <= numero:
        digitos += 1
        i *= 10
    return digitos

def valor_posicional(numero):
    posicion = 1
    j = 1
    while j < contador_digitos(numero):
        posicion *= 10
        j += 1
    return posicion

def digitos(numero):
    digito = numero // valor_posicional(numero)
    return digito

def destripador(numero):
    nuevo_numero = numero - digitos(numero) * valor_posicional(numero)
    return nuevo_numero

#def separador_digitos(numero):
        

#def es_pandigital(numero):

n = int(input("Enter an integer: "))

print("Es primo? "+str(es_primo(n)))


print("Numero de digitos: "+str(contador_digitos(n)))

print("Valor posicional: "+str(valor_posicional(n)))

print("Dígito: "+str(digitos(n)))

print("Nuevo numero: "+str(destripador(n)))
