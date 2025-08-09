def func(nom, lista):
    otra = lista
    for i in range(len(nom)):
        otra.append(nom[0])
        func(nom[1:], otra)

output = []
func("Sol", output)
print(output)
