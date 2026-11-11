'''
  Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una 
  caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.

  Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición 
  en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.

  En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.
'''


class Cuenta:
    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto

    def mostrar(self):
        print("Titular:", self.titular)
        print("Monto:", self.monto)

class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)

    def mostrar(self):
        print("\nCaja de Ahorro")
        super().mostrar()


class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, tasa):
        super().__init__(titular, monto)
        self.plazo = plazo
        self.tasa = tasa

    def mostrar(self):
        print("\nPlazo Fijo")
        super().mostrar()
        print("Plazo:", self.plazo)
        print("Tasa:", self.tasa)


caja_ahorro = CajaAhorro("Juan", 1000)
plazo_fijo = PlazoFijo("Ana", 2000, 30, 0.1)

caja_ahorro.mostrar()
plazo_fijo.mostrar()