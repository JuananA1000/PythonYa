'''
  Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor del lado 
  llegando como parámetro al método __init__ (definir un atributo llamado lado), imprimir su perímetro y su 
  superficie. 
'''

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def mostrar_perimetro(self):
        print("Perímetro: ", self.lado * 4)

    def mostrar_superficie(self):
        print("Superficie: ", self.lado * self.lado)


lado = int(input("Ingrese el lado del cuadrado: "))
cuadrado1 = Cuadrado(lado)
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()
