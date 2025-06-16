'''
  Veamos con un ejemplo la sintaxis para redefinir el operador +.
  Crearemos una clase Cliente de un banco y redefiniremos el operador + para que nos retorne la suma de los depósitos de 
  los dos clientes que estamos sumando.
'''

class Cliente:
    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto

    def __add__(self, otro):
        resultado = self.monto + otro.monto
        return resultado


c1 = Cliente("Juan", 100)
c2 = Cliente("Maria", 150)

print(f"La suma de los depósitos de {c1.nombre} y {c2.nombre} es: {c1 + c2}")
