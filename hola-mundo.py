import math

print("¿Hola mundo?")

a = 23
b = 12
c = a + b
d =3.4
e = True
f = "Python"
frase = "¡Hola, Mundo!"
palabra = "tragasables"

print(palabra.capitalize())

print(frase[7:12])
print(frase[7:12:2])

print(f)
print(type(f))
print(len(f))
print(f[2])
print(f[1:4])
print(f[1:])
print(f[:3])
print(f[:])
print(f[1:6:2])

print("python")
print(type("python"))
print(len("python"))

print(e)
print(type(e))
print(d)
print(type(d))

print(c)
print(type(c))

num = input("Ingrese un numero: ")
print(num)
print(type(num))

num2 = int(input("Ingrese un numero: "))
print(num2)
print(type(num2))

palabra1 = "Hola"
palabra2 = "pendejo"

print(palabra1 + " " + palabra2)

print(15/5)
print(15//5)

print(5.6/3.4)
print(5.6//3.4)

print(2**3)
print(5**2)
print(4.5**4.7)
print(16**(1/2))

print(5%2)
print(16%4)
print(16%6)

print((5<6) and (6>8))

print(f == "python")
print(f != "python")

print("ABC" < "A")
print("A" < "B")
print("B" > "A")

edad = 56
print(edad)
edad += 3
print(edad)
edad -= 2
print(edad)
edad *= 3
print(edad)
edad /= 2
print(edad)

# Comentario1
# Comentario2

temp = 15
if temp < 25:
    print("Frio")
else:
    print("Calor")

#lista

letras = ["a","b","c","d"]

print(letras)
print(letras[3])

nums = [1,2,3,4]

print(nums)
nums.append(5)

print(nums)

nums.insert(3,3.5)

print(nums)

nums2 = [1,2,3,4,5,4]

print(nums2)

nums2.remove(4)

print(nums2)

vocales = ['a','e','i','o','u']

print(vocales)

print('a' in vocales) #operador in para ver si esta un elemento en la lista

print('z' in vocales) #el resiltado es un booleano

print(nums2.index(5))

print(vocales.index('i'))

nums2[4] = 6 #actualiza un elemento de la lista dado un índice

print(nums2)


nos = (3, 5, 2, 8, 4, 6, 3, 2) #tupla

print(nos)
print(nos.count(3))

#diccionario, coleccion de pares clave-valor
#los diccionarios son mutables
#las claves son elementos unicos e inmutables
#los valores pueden ser mutables

edades = {"Gino": 15, "Nora": 45}

print(edades)
print(edades["Gino"])
print(edades["Nora"])

print(edades.get("Gino"))

edades["Talina"] = 67

print(edades)

edades["Gino"] = 17

print(edades)

del edades["Gino"]

print(edades)

print("Gino" in edades)
print("Nora" in edades)
print("Emily" in edades)

for i in range(4):
    print(i)

for i in range(0,101,10):
    print(i)

for char in "Loops":
    print(char)

for num in [1,2,3,4]:
    print(num)

for num in (1,2,3):
    print(num)

letras = {"a": 1, "b": 2}

for clave in letras:
    print(clave)

for valor in letras.values():
    print(valor)

for clave, valor in letras.items():
    print(clave, valor)
    
x = 20

while x < 35:
    print(x)
    x += 3

def mostrar_mensaje():
    print("¡Hola, Mundo!")

mostrar_mensaje()

mostrar_mensaje()

mostrar_mensaje()

def sumar(x,y):
    print(x + y)

sumar(4,5)

resultado = sumar(4,5)

print(resultado)

def multiplicar(x,y):
    return x*y

resultado = multiplicar(4,5)

print(resultado)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

with open("frases_famosas.txt", "r") as archivo:
    for linea in archivo:
        print("==== Frase ====")
        print(linea)

notas = {
        "Nora": 87,
        "Gino": 100,
        "Loretto": 67,
        "Talina": 45
}

with open("data_estudiantes.txt", 'w') as archivo:
    for hombre, notario in notas.items():
        archivo.write(hombre + " - " + str(notario) + "\n")

nuevas_notas = {
        "Emily": 54,
        "Tragasables": 1000,
        "G.Profunda": 100
}

with open("data_estudiantes.txt", 'a') as archivo:
    for nombre, nota in nuevas_notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")

print(math.pow(9, 2))

print(math.pi)

from math import pow #importa solo un elemento del modulo y no todo el modulo

print(pow(9,2))


