'''
  Plantear una clase Rectangulo. Definir dos atributos (lado_menor y lado_mayor). Redefinir el operador == de tal forma 
  que tengan en cuenta la superficie del rectángulo. Lo mismo hacer con todos los otros operadores relacionales.
'''

class Rectangulo:
    def __init__(self, lado_menor, lado_mayor):
        self.lado_menor = lado_menor
        self.lado_mayor = lado_mayor

    def __eq__(self, otro):
        return self.lado_menor == otro.lado_menor and self.lado_mayor == otro.lado_mayor

    def __gt__(self, otro):
        return self.lado_menor > otro.lado_menor and self.lado_mayor > otro.lado_mayor

    def __lt__(self, otro):
        return self.lado_menor < otro.lado_menor and self.lado_mayor < otro.lado_mayor

    def __ge__(self, otro):
        return self.lado_menor >= otro.lado_menor and self.lado_mayor >= otro.lado_mayor

    def __le__(self, otro):
        return self.lado_menor <= otro.lado_menor and self.lado_mayor <= otro.lado_mayor


rect1 = Rectangulo(10, 10)
rect2 = Rectangulo(5, 20)

if rect1 == rect2:
    print("Los rectangulos tienen la misma superficie")
else:
    print("Los rectangulos no tienen la misma superficie")
