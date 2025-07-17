nombre = "Dr. Nick"
saludo = "Hola,"
pregunta = "¿cómo estás hoy?"
print(saludo, nombre, pregunta)

nombre = input("¿Cuál es tu nombre?")
print(saludo, nombre, pregunta)

lec = int(input("¿Cuántas lecciones has visto?"))
total = 15
faltan = total - lec
print("Te faltan ", faltan, "lecciones. ¡Ánimo!")

monedas = int(input("¿Cuántas monedas tienes?"))
siguiente = monedas + 1
print("Yo tengo más. Tengo", siguiente)

t = float(input("¿En cuántos segs corres 100m?"))
dif = t - 9.58
print("Eres ", dif, "segundos más lento que Bolt")

ingreso = bool(input("Ingresa tu nombre: "))
print("Nombre ingresado: ", ingreso)

