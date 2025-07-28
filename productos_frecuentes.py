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

def productos_frecuentes(boletas):
    productos_boleta = []
    productos_comprados = set()
    for boleta in boletas:
        productos_boleta = productos_boleta + list(boleta["productos"])
        productos_comprados = set(productos_boleta)

    frecuencia = []
    productos_frecuentes = set()
    for elem in productos_comprados:
        frecuencia = productos_boleta.count(elem)
        porcentaje = frecuencia / len(boletas)
        if porcentaje >= 0.5:
            productos_frecuentes.add(elem)

    return productos_frecuentes

print(productos_frecuentes(boletas))

        


    

