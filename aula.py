class Aula:
    def __init__(self, p):
        self.profesor = p
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def imprimir_mejor_nota(self):
        mejor = 0
        for estudiante in self.estudiantes:
            if estudiante.nota_final > mejor:
                mejor = estudiante.nota_final
        print(mejor)

class Estudiante:
    def __init__(self, nom, nota):
        self.nombre = nom
        self.nota_final = nota

class Profesor:
    def __init__(self, n):
        self.nombre = n

profesor = Profesor( 'Calamardo' )
e1 = Estudiante( 'Bob', 6 )
e2 = Estudiante( 'Patricio', 2 )
e3 = Estudiante( 'Arenita', 7 )

aula = Aula(profesor)
aula.agregar_estudiante(e1)
aula.agregar_estudiante(e2)
aula.agregar_estudiante(e3)

aula.imprimir_mejor_nota()
