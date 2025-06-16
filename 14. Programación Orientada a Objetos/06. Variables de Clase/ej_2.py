'''
  Plantear una clase llamada Jugador.
  Definir en la clase Jugador los atributos nombre y puntuación, y los métodos __init__, imprimir y pasar_tiempo (que debe 
  reducir en uno la variable de clase).
  Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el fin de juego 
  (iniciarla con el valor 30)
  Definir en el bloque principal dos objetos de la clase Jugador.
  Reducir dicha variable hasta llegar a cero.
'''

class Jugador:
    minutos = 30

    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Puntuación:", self.puntuacion)
        print("Minutos:", self.minutos)

    def pasar_tiempo(self):
        self.minutos -= 1

        if self.minutos == 0:
            print("\nFin del juego")
            exit()


jugador1 = Jugador("Juan", 100)
jugador2 = Jugador("Ana", 200)

jugador1.imprimir()
jugador2.imprimir()

while Jugador.minutos > 0:
    jugador1.pasar_tiempo()
    jugador2.pasar_tiempo()
    jugador1.imprimir()
    jugador2.imprimir()
