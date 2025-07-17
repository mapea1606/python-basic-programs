no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]
print("Hay", len(no_olvidar), "cosas por comprar")
no_olvidar.append("jamón")
print("Hay", len(no_olvidar), "cosas por comprar")
print("¿Debo comprar vino?", ("vino" in no_olvidar))
print("¿Debo comprar palta?", ("palta" in no_olvidar))
print("Lechuga:", no_olvidar.index("lechuga"))

