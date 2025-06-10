'''
  Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo. En el método __init__
  cargar los atributos por teclado y luego en otro método imprimir sus datos y por último uno que imprima un mensaje si 
  debe pagar impuestos (si el sueldo supera a 3000) 
'''

class Empleado:
    def __init__(self):
        self.nombre = input("Nombre del empleado: ")
        self.sueldo = int(input("Sueldo del empleado: "))

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Sueldo: ", self.sueldo)

    def mostrar_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")


empleado1 = Empleado()
empleado1.mostrar()
empleado1.mostrar_impuestos()