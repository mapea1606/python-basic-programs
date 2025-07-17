llueve = True
temperatura = int(input("Ingresa temp°"))
if temperatura < 18:
    if llueve == True:
        print("Llevaré paraguas y abrigo")
    else:
        print("Solo llevaré abrigo")
else:
    print("No necesito paraguas ni abrigo")

llueve = True
temperatura = int(input("Ingresa temp°"))
if temperatura < 18 and llueve == True:
    print("Llevaré paraguas y abrigo")
elif temperatura < 18 and llueve == False:
    print("Solo llevaré abrigo")
else:
    print("No llevaré paraguas ni abrigo")

llueve = True
temperatura = int(input("Ingresa temp°"))
if temperatura >= 18:
    print("No llevaré paraguas ni abrigo")
elif llueve == True:
    print("Llevaré paraguas y abrigo")
else:
    print("Solo llevaré abrigo")
