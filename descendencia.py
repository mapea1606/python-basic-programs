def encontrar_padres(arbol, nombre):
    # La tupla principal es la raíz del árbol (padre y su lista de hijos).
    padre, hijos = arbol
    
    # Caso 1: El nombre buscado es el padre actual (caso base).
    if padre == nombre:
        return [nombre]
    
    # Caso 2: Buscar en los hijos del padre actual.
    for hijo_arbol in hijos:
        # Llamada recursiva para buscar en la rama de cada hijo.
        resultado = encontrar_padres(hijo_arbol, nombre)
        
        # Si la llamada recursiva encontró el nombre (no retornó False)...
        if resultado:
            # Añade el nombre del padre actual a la lista de padres y retorna la lista.
            resultado.append(padre)
            return resultado
    
    # Si el nombre no se encuentra en esta rama, retorna False.
    return False

# Estructura del árbol de descendencia
descendencia = ('Eligio', [
                        ('Celestina', [
                                ('Carmela', []),
                                ('Rosendo', [
                                        ('José', []),
                                        ('Anastacia', [])
                                ])
                        ]),
                        ('Julián', [
                                ('Fabián', [
                                        ('Berto', []),
                                        ('Fausto', []),
                                        ('Abel', []),
                                        ('Florina', [])
                                ]),
                        ])
])

# Ejemplos de uso
print(f"encontrar_padres(descendencia, 'Fausto') -> {encontrar_padres(descendencia, 'Fausto')}")
print(f"encontrar_padres(descendencia, 'Celestina') -> {encontrar_padres(descendencia, 'Celestina')}")
print(f"encontrar_padres(descendencia, 'Jorge') -> {encontrar_padres(descendencia, 'Jorge')}")
