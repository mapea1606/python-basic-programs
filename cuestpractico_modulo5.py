import string

def mezclador(string_a, string_b):
    tamaño_b = len(string_b)
    mezcla = string_a[0:2] + string_b[tamaño_b-2:tamaño_b]
    return mezcla

mezcla = mezclador("puritano", "lagarto")

print(mezcla)

def intercalar(string_a, string_b):
    tamaño_a = len(string_a)
    i = 0
    mezcla = ""
    while i < tamaño_a:
        mezcla = mezcla + string_a[i]
        mezcla = mezcla + string_b
        i = i + 1
    return mezcla

intercalador = intercalar("paz", "so")

print(intercalador)

def ocurrencias(string):
    tamaño = len(string)
    i = 0
    unos = 0
    ceros = 0
    while i < tamaño:
        if string[i] == "0":
            ceros = ceros + 1
        else:
            unos = unos + 1
        i = i + 1
    return unos - ceros

diferencia = ocurrencias("11000110101")

print(diferencia)
            
def remover_enesimo(s, n):
    t = len(s)
    if n > 0 and n < t - 1:
        return s[0:n] + s[n + 1:t]
    elif n == 0:
        return s[1:t]
    elif n == t - 1:
        return s[0:t - 1]

s_nueva = remover_enesimo("Hasta luego", 3)
print(s_nueva)

s_nueva = remover_enesimo("Hasta luego", 0)
print(s_nueva)

s_nueva = remover_enesimo("Hasta luego", 10)
print(s_nueva)
       
print(string.ascii_uppercase)
print(len(string.ascii_uppercase))
print(len("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def reemplazo(string):
    mayuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    while i < len(string):
        j = 0
        while j < len(mayuscula):
            if string[i] == mayuscula[j]:
                string = string.replace(string[i],"$")
            j = j + 1
        i = i + 1
    return string

reemplazada = reemplazo("Y cuando desperto, el DINOSAURIO todavía estaba ahi")

print(reemplazada)



