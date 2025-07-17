# uno

lista = [1, 2, 4, 5, 6, 7, 8, 9]
lista.insert(2, 3)
print(lista)

# dos

lista = [1, 2, 7, 4, 5, 6, 3, 8, 9]
lista[2] = 3
lista[6] = 7
print(lista)

# seis

lista = ['soleado', 'nublado', 'soleado', 'lluvia', 2.4, 'lluvia', 0.1, 'nublado', 'lluvia', 0.8]

suma = 0
for i in lista:
    if i not in ['soleado', 'nublado', 'lluvia']:
        suma += i
print(suma)
