class Libro:
    def __init__(self, t, a, g):
        self.titulo = t
        self.autor = a
        self.genero = g
        
    def __str__(self):
        return self.titulo

L1 = Libro('Harry Potter', 'J. K. Rowling', 'Fantasía')
L2 = Libro('Juego de tronos', 'George R. R. Martin', 'Novela')
L3 = Libro('El señor de los anillos', 'J. R. R. Tolkien', 'Novela')

biblioteca = [L1, L2, L3]

for libro in biblioteca:
    if libro.genero == 'Novela':
        print(libro)
