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

def precio_total(boletas):
    total = 0
    for boleta in boletas:
        total = total + boleta["precio"]
    return total

print(precio_total(boletas))
        
