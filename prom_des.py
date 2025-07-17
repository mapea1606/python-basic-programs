import math

def promedio_std(lista):
    suma = 0
    suma_cuad = 0
    contador = 0

    for elem in lista:
        suma = suma + elem
        contador += 1

    promedio = suma / contador

    for elem in lista:
        suma_cuad = suma_cuad + (elem - promedio) ** 2

    desviacion_e = math.sqrt(suma_cuad / contador) 
    
    return (promedio, desviacion_e)

numeros = [43,87,74,55,83,73,57,4,26,9,37,42,46,94,34,31,42,2]

(prom, des_est) = promedio_std(numeros)

print(prom)
print(des_est)
        

