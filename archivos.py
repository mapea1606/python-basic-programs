lectura = open("arch.txt", "r")

leer = lectura.read()
print(leer)

leer = lectura.readline()
print(leer)

leer2 = lectura.readline()
print(leer2)

escritura = open("arch.txt", "w")

escribir = escritura.write("uno\ndos\ntres\ncuatro\ncinco")

escritura.close()
