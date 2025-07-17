no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]
print(type(no_olvidar))
print(no_olvidar)
print(no_olvidar[2])
print(no_olvidar[1:4])

no_olvidar.append("apio")
print(no_olvidar)

no_olvidar.extend(["apio", "tomates"])
print(no_olvidar)
print(no_olvidar[5])

no_olvidar.insert(6, 5000)
print(no_olvidar)
print(no_olvidar[6])

comprado = no_olvidar.pop()
print(no_olvidar)
print("Ya compré", comprado)

comprado = no_olvidar.pop(3)
print(no_olvidar)
print("Ya compré", comprado)

for elem in no_olvidar:
    print("No olvides", elem)

tambien = ["apio", "tomates"]
no_olvidar = no_olvidar + tambien
print(no_olvidar)
print(tambien * 2)

no_olvidar[1] = "queso"
no_olvidar[3] = 10000
print(no_olvidar)


