numero = int(input("Ingrese calidad del aire"))
if numero >= 0 and numero <= 99:
  print("Bueno")
elif numero >= 100 and numero <= 199:
  print("Regular")
elif numero >= 200 and numero <= 299:
  print("Alerta")
elif numero >= 300 and numero <= 499:
  print("Preemergencia")
else:
  print("Emergencia")

a = int(input("Ingrese el año"))

if (a % 4 == 0 and a % 100 != 0) or (a % 100 == 0 and a % 400 == 0):
    print("Es bisiesto")
