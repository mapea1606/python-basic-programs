ejemplo = open("ejemplo.txt", "r")
a = ejemplo.readline()
b = ejemplo.readline()
c = ejemplo.readline()
d = a + c
print(d)

a = open("mooc.txt")
linea = a.readline()
linea = a.readline()
linea = a.readline()
linea = a.readline()
print(linea)

a = open("mooc.txt", "w")
a.write("1 2 3 4")
a.write("5 6 7 8")
a.close()
