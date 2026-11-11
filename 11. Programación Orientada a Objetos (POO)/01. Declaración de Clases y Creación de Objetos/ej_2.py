'''
  Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para 
  inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4).

  Definir dos objetos de la clase Alumno.
'''

class Alumno:
    def inicializar(self, nom, nota):
        self.nombre = nom
        self.nota = nota

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def mostrar_estado(self):
        if self.nota >= 4:
            print("Regular")
        else:
            print("Libre")


alumno1 = Alumno()
print("\nAlumno 1")
alumno1.inicializar("Juan", 4)
alumno1.mostrar()
alumno1.mostrar_estado()

alumno2 = Alumno()
print("\nAlumno 2")
alumno2.inicializar("Ana", 3)
alumno2.mostrar()
alumno2.mostrar_estado()
