def func(n, s):
    if n == 0:
        return 0
    for i in range(n):
        s.append("a")
        func(n-1, s)

s = list()
func(5, s)

#print(s)
print(len(s))

#####################


def func2(n):
    s.append("a")
    if n == 0:
        return 0
    print(n/2+1)
    return func2(n/2+1)

func2(16)
