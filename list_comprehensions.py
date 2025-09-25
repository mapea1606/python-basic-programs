if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    X = list()
    i = 0
    while i <= x:
        X.append(i)
        i += 1

    Y = list()
    j = 0
    while j <= y:
        Y.append(j)
        j += 1

    Z = list()
    k = 0
    while k <= z:
        Z.append(k)
        k += 1

    print(f"{X},{Y},{Z}")
    
