'''
  Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los 
  atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase 
  llamarla Triangulo.
'''

class Triangulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mostrar_lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor es: ", self.lado1)
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El lado mayor es: ", self.lado2)
        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
            print("El lado mayor es: ", self.lado3)
        else:
            print("Los lados son iguales")

    def mostrar_tipo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")


triangulo1 = Triangulo()
print("\nTriangulo 1")
triangulo1.inicializar(3, 3, 3)
triangulo1.mostrar_lado_mayor()
triangulo1.mostrar_tipo()

triangulo2 = Triangulo()
print("\nTriangulo 2")
triangulo2.inicializar(3, 4, 5)
triangulo2.mostrar_lado_mayor()
triangulo2.mostrar_tipo()
