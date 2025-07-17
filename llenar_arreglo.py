i = 0
#vector = [1,2,3,4,5,6,7]
vector = list()
while i < 7:
    elem = int(input("Escribe el elemento: "))
    vector.append(elem)
    #print(vector[i])
    i += 1

for elem in vector:
    print(elem)
