class Estudiante:
    def __init__(self, nom):
        self.nombre = nom
        self.notas = []

    def __add__(self, nota):
        self.notas.append(nota)

eva = Estudiante('Eva')

eva + 6.8
eva + 5.6

print(eva.notas)
