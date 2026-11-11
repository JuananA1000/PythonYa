'''
  Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e inmediatamente muestre su 
  suma, resta, multiplicación y división. Hacer cada operación en otro método de la clase Operación y llamarlos desde el 
  mismo método __init__
'''

class Operacion:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        suma = self.valor1 + self.valor2
        print(f"\n{self.valor1} + {self.valor2} = {suma}")

    def resta(self):
        resta = self.valor1 - self.valor2
        print(f"{self.valor1} - {self.valor2} = {resta}")

    def multiplicacion(self):
        multiplicacion = self.valor1 * self.valor2
        print(f"{self.valor1} * {self.valor2} = {multiplicacion}")

    def division(self):
        division = self.valor1 / self.valor2
        print(f"{self.valor1} / {self.valor2} = {division:.2f}")


operacion = Operacion()
