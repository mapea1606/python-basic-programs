x = 1
i = 0
while i < 4:
    x = x * 2
    i += 1
print(x)

x = 48
y = 8
n = 0
while x > 0:
    x = x - y
    n = n + 1
print(n)

a = 5
b = 8
r = 0
while a > 0:
    r = r + b
    a = a - 1
print(r)

a = 4
b = 3
r = b
while a > 1:
    a = a - 1
    b2 = b
    r2 = 0
    while b2 > 0:
        r2 = r2 + r
        b2 = b2 - 1
    r = r2
print(r)

a = 3
for i in range(2,3):
    a = a * i
print(a)

a = 2
for i in range(1,4):
    a = i ** a
print(a)

for i in range(10):
    print('hola mundo')

a = 0
for i in range(3):
    a = a + i
print(a)

numero = 1
while numero <= 5:
    print(numero, numero**2)
    numero = numero + 1

for i in range(1,101):
    for j in range(1,101):
        print(i,j)

