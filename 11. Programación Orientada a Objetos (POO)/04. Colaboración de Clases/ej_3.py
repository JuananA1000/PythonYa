'''
  Plantear una clase Club y otra clase Socio.
  La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
  En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
  La clase Club debe tener como atributos 3 objetos de la clase Socio.
  Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.
'''

class Socio:
    def __init__(self, nombre, antiguedad):
        self.nombre = nombre
        self.antiguedad = antiguedad

class Club:
    def __init__(self):
        self.socio1 = Socio(input("Nombre del socio: "), int(input("Antigüedad del socio: ")))
        self.socio2 = Socio(input("Nombre del socio: "), int(input("Antigüedad del socio: ")))
        self.socio3 = Socio(input("Nombre del socio: "), int(input("Antigüedad del socio: ")))

    def mayor_antiguedad(self):
        if self.socio1.antiguedad > self.socio2.antiguedad and self.socio1.antiguedad > self.socio3.antiguedad:
            print(f"El socio {self.socio1.nombre} tiene la mayor antigüedad en el club con {self.socio1.antiguedad} años.")
        elif self.socio2.antiguedad > self.socio1.antiguedad and self.socio2.antiguedad > self.socio3.antiguedad:
            print(f"El socio {self.socio2.nombre} tiene la mayor antigüedad en el club con {self.socio2.antiguedad} años.")
        else:
            print(f"El socio {self.socio3.nombre} tiene la mayor antigüedad en el club con {self.socio3.antiguedad} años.")

club = Club()
club.mayor_antiguedad()
