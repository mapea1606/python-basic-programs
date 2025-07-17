def funcion_misteriosa(x):
    for i in range(2,x):
        if x%i==0:
            return False
        return True

print(funcion_misteriosa(102))
print(funcion_misteriosa(103))

def funcion_misteriosa_2(x):
    c = 0
    while x != 0:
        c += 1
        x = x // 10
    return c

print(funcion_misteriosa_2(295))
