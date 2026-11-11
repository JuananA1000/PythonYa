'''
  Desarrollar un programa que implemente una clase llamada Jugador.
  Definir como atributos su nombre y puntuación.
  Codificar el método especial __str__ que retorne el nombre y si es principiante (menos de 1000 puntos) o experto (1000 
  o más puntos).
'''

class Jugador:

    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

    def __str__(self):
        if self.puntuacion < 1000:
            return f"{self.nombre} | Puntuación: {self.puntuacion} -> PRINCIPIANTE"
        else:
            return f"{self.nombre} | Puntuación: {self.puntuacion} -> EXPERTO"


j1 = Jugador("Juan", 100)
j2 = Jugador("Pedro", 2000)
j3 = Jugador("Luis", 1000)
j4 = Jugador("Ana", 200)

print(j1)
print(j2)
print(j3)
print(j4)
