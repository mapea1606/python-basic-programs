string1 = "La casa"
string2 = " es verde"
string3 = string1 + string2

print(string3)

print("animal " * 10)

a = "martes"

print(a + " miercoles")

print("Martes" [0])

print("Martes" [5])
print("Martes" [-1])

print("Martes" [1:4])

print("Un párrafo. \nOtro párrafo.")

x = "abracadabra"

print(x[3:6])

print(len("Yo soy."))

print("Jueves".upper())
print("JUeves".lower())

a = "Bien. Martes a las 5."

print(a.strip("."))

a = "Hola!!1!"

print(a.replace("1", "!"))

s = input("Ingresa una palabra: ")
resultado = ""
i = 0
while i < len(s):
    resultado = resultado + s[len(s)-i-1]
    i = i + 1
print(resultado)
