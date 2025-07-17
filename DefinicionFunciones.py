def max_divisor(n):
    maximo_actual = 0
    i = 1
    while i < n:
        if n % i == 0:
            maximo_actual = i
        i += 1
    return maximo_actual

print(max_divisor(125))

def potencia_positiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        resultado = 1
        while exponente > 0:
            resultado *= base
            exponente -= 1
        return resultado

print(potencia_positiva(3,5))
