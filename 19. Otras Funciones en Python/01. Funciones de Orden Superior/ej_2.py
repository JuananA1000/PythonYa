'''
  Declarar una clase que almacene el nombre y la edad de una persona. Definir un método que retorne True o False según 
  si la persona es mayor de edad o no. Este método debe recibir como parámetro una función que al llamarla pasando la 
  edad de la persona retornará si es mayor o no de edad.
  
  Tener en cuenta que una persona es mayor de edad en Estados Unidos si tiene 21 o más años y en Argentina si tiene 18 
  o más años.
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor(self, fn):
        return fn(self.edad)

    def mayor_esp(edad):
        if edad >= 18:
            return True
        else:
            return False

    def mayor_usa(edad):
        if edad >= 21:
            return True
        else:
            return False


persona = Persona("juan", 18)

if persona.es_mayor(Persona.mayor_esp):
    print(f"{persona.nombre} es mayor de edad en España")
else:
    print(f"{persona.nombre} no es mayor de edad en España")

if persona.es_mayor(Persona.mayor_usa):
    print(f"{persona.nombre} es mayor de edad en Estados Unidos")
else:
    print(f"{persona.nombre} no es mayor de edad en Estados Unidos")
