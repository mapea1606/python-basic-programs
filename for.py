print("°F   °C")
for temp in range(32,73):
    print(temp, "   ", int((temp-32)*5/9))

for i in range(1,100):
    if i < 18:
        print(i, "menor de edad")
    else:
        print(i, "mayor de edad")
