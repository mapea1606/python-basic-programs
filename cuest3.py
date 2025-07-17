#pregunta1
x = 1
i = 0
while i < 4:
    x = x * 2
    i += 1
print(x)

#pregunta2
x = 48
y = 8
n = 0
print("x//y =", x//y, end=", n = ")
while x > 0:
    x = x - y
    n = n + 1
print(n)

#pregunta3
a = 5
b = 8
r = 0
while a > 0:
    r = r + b
    a = a - 1
print(r)

#pregunta4
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

#pregunta5
a = 3
for i in range(2, 3):
    a = a * i
print(a)

#pregunta6
a = 2
for i in range(1, 4):
    a = i ** a
print(a)

#pregunta7
for i in range(10):
    print("Hola mundo")

#pregunta8
a = 0
for i in range(3):
    a = a + i
print(a)

#pregunta9
numero = 1
#while numero <= 5:
#    print(numero, numero**2)

#pregunta10
for i in range(1, 101):
    for j in range(1, 101):
        print(i, j)

