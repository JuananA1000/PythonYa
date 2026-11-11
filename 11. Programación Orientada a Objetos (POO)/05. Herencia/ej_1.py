'''
  Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades la carga por 
  teclado y su impresión.
  En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

  Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si 
  debe pagar impuestos (sueldo superior a 3000). También en el bloque principal del programa crear un objeto de la 
  clase Empleado.
'''

class Persona:
    def __init__(self):
        print("\nIngrese los datos de la persona")
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))

    def imprimir(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad}")

class Empleado(Persona):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre (Persona)

        print("\nIngrese los datos del empleado")
        self.sueldo = int(input("Sueldo: "))

    def imprimir(self):
        super().imprimir()
        print(f"Sueldo: {self.sueldo}")

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print(f"{self.nombre} debe pagar impuestos")
        else:
            print(f"{self.nombre} NO debe pagar impuestos")


p1 = Persona()
p1.imprimir()

e1 = Empleado()
e1.imprimir()
e1.pagar_impuestos()
