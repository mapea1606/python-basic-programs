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

boletas2 = [{'fecha_compra': '11-06-22', 'precio': 15000, 'productos': {'Chocolate': 4}}, {'fecha_compra': '25-06-22', 'precio': 18000, 'productos': {'Leche': 4, 'Huevos': 3}}, {'fecha_compra': '12-05-22', 'precio': 19000, 'productos': {'Leche': 5, 'Pan': 3, 'Chocolate': 4}}, {'fecha_compra': '23-06-22', 'precio': 18000, 'productos': {'Pan': 6, 'Chocolate': 3, 'Mantequilla': 2}}, {'fecha_compra': '24-05-22', 'precio': 15000, 'productos': {'Leche': 2, 'Huevos': 2, 'Azucar': 3, 'Pan': 5}}]

def precio_mes(boletas):

    precio_fecha = dict()

    for boleta in boletas:
        precio_fecha[boleta["fecha_compra"]] = boleta["precio"] 
    
    fecha = list(precio_fecha)
    meses = []
    for elem in fecha:
        meses.append(elem[3:])

    meses = set(meses)
    
    total_mensual = []

    for elem in precio_fecha.items():
        total_mensual.append((elem[0][3:],elem[1]))

    total_mensual.sort()
    mensualidad = 0
    precio_mes = dict()
    for mes in meses:
        mensualidad = 0
        for elem in total_mensual:
            if elem[0] == mes:
                mensualidad = mensualidad + elem[1]
                precio_mes[elem[0]] = mensualidad

    print(total_mensual)


    return precio_mes

def precio_mes2(boletas):

    precio_fecha = dict()
    for boleta in boletas:
        precio_fecha[boleta["fecha_compra"]] = boleta["precio"]

    cuentas_mes = list()
    for t in precio_fecha.items():
        cuentas_mes.append((t[0][3:],t[1]))
    cuentas_mes.sort()

    meses = []
    for elem in cuentas_mes:
        meses.append(elem[0])
    meses = set(meses)

    precio_mes = dict()
    for mes in meses:
        mensualidad = 0
        for elem in cuentas_mes:
            if elem[0] == mes:
                mensualidad = mensualidad + elem[1]
                precio_mes[elem[0]] = mensualidad

    return precio_mes



print(precio_mes2(boletas2))


    
        
