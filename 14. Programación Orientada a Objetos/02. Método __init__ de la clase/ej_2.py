'''
  Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores de 
  'x' e 'y' que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático, primer 
  cuadrante si 'x' e 'y' son positivas, si 'x' < 0 e 'y' > 0 segundo cuadrante, etc.)
'''

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        print("\nCoordenadas: ", self.x, self.y)

    def mostrar_cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print("Segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print("Cuarto cuadrante")
        else:
            print("Origen")


punto1 = Punto(1, 2)
punto1.mostrar_coordenadas()
punto1.mostrar_cuadrante()

punto2 = Punto(-1, 2)
punto2.mostrar_coordenadas()
punto2.mostrar_cuadrante()

punto3 = Punto(-1, -2)
punto3.mostrar_coordenadas()
punto3.mostrar_cuadrante()

punto4 = Punto(1, -2)
punto4.mostrar_coordenadas()
punto4.mostrar_cuadrante()

punto5 = Punto(0, 0)
punto5.mostrar_coordenadas()
punto5.mostrar_cuadrante()
