def mcd(n1, n2):
    r = n1 % n2
    q = n1 // n2

    while r != 0:
        n1 = n2
        n2 = r
        r = n1 % n2
        q = n1 // n2

        if r == 0:
            return n2 

a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))

mcd = mcd(a,b)

print("mcd("+str(a)+","+str(b)+")= "+str(mcd))
