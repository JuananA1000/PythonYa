'''
  Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__, calcular su 
  suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados. 
'''

class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: No se puede dividir por cero"

    def mostrar_resultados(self):
        print(f"\n{self.valor1} + {self.valor2} = {self.suma()}")
        print(f"{self.valor1} - {self.valor2} = {self.resta()}")
        print(f"{self.valor1} * {self.valor2} = {self.multiplicacion()}")
        print(f"{self.valor1} / {self.valor2} = {self.division():.2f}")


operacion = Operaciones()
operacion.mostrar_resultados()
