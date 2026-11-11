'''
  Crear una clase Persona que tenga como atributo el nombre y la edad.
  El operador == retornará verdadero si las dos personas tienen la misma edad, el operador > retornará True si la edad 
  del objeto de la izquierda tiene una edad mayor a la edad del objeto de la derecha del operador >, y así 
  sucesivamente.
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otro):
        return self.edad == otro.edad

    def __gt__(self, otro):
        return self.edad > otro.edad

    def __lt__(self, otro):
        return self.edad < otro.edad

    def __ge__(self, otro):
        return self.edad >= otro.edad

    def __le__(self, otro):
        return self.edad <= otro.edad


p1 = Persona("Juan", 47)
p2 = Persona("Maria", 30)

if p1 == p2:
    print(f"{p1.nombre} y {p2.nombre} tienen la misma edad")
else:
    if p1 > p2:
        print(f"{p1.nombre} es mayor que {p2.nombre}")
    else:
        print(f"{p2.nombre} es mayor que {p1.nombre}")
