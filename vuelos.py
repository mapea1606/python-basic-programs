vuelos = [["Origen", "Destino", "precio", "asientos disponibles", "Fecha"],
          ["Santiago", "Puerto Montt", 35000, 30, "11 Enero 2023"],
          ["Santiago", "Concepción", 30000, 40, "20 Febrero 2023"],
          ["Santiago", "Puerto Montt", 28000, 2, "19 Enero 2023"],
          ["Santiago", "Puerto Montt", 12000, 100, "20 Mayo 2023"],
          ["Antofagasta", "Santiago", 27000, 14, "18 Abril 2023"]]

def vuelos_disponibles(vuelos, origen, destino, pasajeros):
    resultado = []
    resultado.append(vuelos[0])
    for vuelo in vuelos:
        if vuelo[0] == origen and vuelo[1] == destino and vuelo[3] >= pasajeros:
            resultado.append(vuelo)
    return resultado

print(vuelos_disponibles(vuelos, "Santiago", "Puerto Montt", 5))


