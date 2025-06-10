'''
  Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados. 
  Imprimir un mensaje si es mayor de edad (edad >= 18) 
'''

class Persona:
    def inicializar(self, nom, edad):
        self.nombre = nom
        self.edad = edad

    def mostrar_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} tiene {self.edad} años -> es mayor de edad")
        else:
            print(f"{self.nombre} tiene {self.edad} años -> es menor de edad")


persona1 = Persona()
print("\nPersona 1")
persona1.inicializar("Juan", 22)
persona1.mostrar_mayor_de_edad()

persona2 = Persona()
print("\nPersona 2")
persona2.inicializar("Ana", 15)
persona2.mostrar_mayor_de_edad()
