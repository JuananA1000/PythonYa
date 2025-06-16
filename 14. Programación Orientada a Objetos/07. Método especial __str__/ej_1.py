'''
  Definir una clase llamada Punto con dos atributos x e y.
  Crearle el método especial __str__ para retornar un string con el formato (x, y).
'''

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Punto ({self.x}, {self.y})'


p1 = Punto(34, 5)
p2 = Punto(2, 45)

print(p1)
print(p2)
