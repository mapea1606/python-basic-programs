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

def precio_mes(boletas):
    precio_mes = dict()
    total_mes = 0
    for boleta in boletas:
        precio_mes[boleta["fecha_compra"][3:]] = 0        
        for elem in precio_mes:
            if elem == boleta["fecha_compra"][3:]:
                total_mes = total_mes + boleta["precio"]
                precio_mes[elem] = total_mes
            elif elem != boleta["fecha_compra"][3:]:
                total_mes = 0
    return precio_mes

print(precio_mes(boletas))


    
        
