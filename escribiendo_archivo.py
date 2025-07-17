s = input("Ingresa nombre archivo: ")
t = open(s)
l = t.readline()
while l!="":
  print(l)
  l=t.readline()
