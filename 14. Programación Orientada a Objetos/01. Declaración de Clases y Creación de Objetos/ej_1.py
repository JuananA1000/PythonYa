'''
  Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos (funciones), 
  uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la pantalla el contenido 
  del mismo.

  Definir dos objetos de la clase Persona.
'''

class Persona:
    def inicializar(self, nom):
        self.nombre = nom

    def mostrar(self):
        print("Nombre: ", self.nombre)


persona1 = Persona()
print("\nPersona 1")
persona1.inicializar("Juan")
persona1.mostrar()

persona2 = Persona()
print("\nPersona 2")
persona2.inicializar("Ana")
persona2.mostrar()
