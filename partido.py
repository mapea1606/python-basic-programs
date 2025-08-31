equipos = [('Equipo 1', 5),
           ('Equipo 2', 7),
           ('Equipo 3', 8),
           ('Equipo 4', 2),
           ('Equipo 5', 9),
           ('Equipo 6', 1),
           ('Equipo 7', 3),
           ('Equipo 8', 4)]

def partido(equipos):
    if len(equipos) == 1:
        return equipos[0]

    mitad = len(equipos)//2
    gan_izq = partido(equipos[:mitad])
    gan_der = partido(equipos[mitad:])
    nom1, hab1 = gan_izq
    nom2, hab2 = gan_der

    if hab1 > hab2:
        print('Gana: ' + nom1)
        return equipos[0]
    else:
        print('Gana: ' + nom2)
        return equipos[1]

partido(equipos)
