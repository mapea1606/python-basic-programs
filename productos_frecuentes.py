boletas = [{"fecha_compra" : "29-05-22",
            "precio" : 12000,
            "productos" : {"Chocolate" : 1,
                           "Mantequilla" : 1,
                           "Huevos" : 12,
                           "Pan" : 1}
            },
           {"fecha_compra" : "31-05-22",
            "precio" : 2400,
            "productos" : {"Pan" : 1, "Leche" : 2}
            },
           {"fecha_compra" : "01-06-22",
            "precio" : 3000,
            "productos" : {"Mantequilla": 2, "Azucar" : 1}
            }]
i = 0
productos_boleta = []
productos_comprados = set()
for boleta in boletas:
    productos_boleta.append(set(boleta["productos"]))
    productos_comprados = productos_comprados | productos_boleta[i]
    i += 1

for elem in productos_boleta:
    print(productos_comprados & elem)
    
print(productos_comprados)
    

