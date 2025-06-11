'''
  Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú de opciones que 
  permita:
  a) Cargar alumnos.

  b) Listar alumnos.

  c) Mostrar alumnos con notas mayores o iguales a 7.

  d) Finalizar programa.
'''

class Agenda:
    def __init__(self):
        self.nombres = []
        self.notas = []

    def cargar_alumnos(self):
        for i in range(5):
            print("\nIngrese los datos de 5 alumnos:")
            print(f"|-- Alumno [{i+1}] --|")
            nombre = input("Nombre: ")
            nota = float(input("Nota: "))

            self.nombres.append(nombre)
            self.notas.append(nota)

    def listar_alumnos(self):
        print("\nAlumnos")
        for i in range(5):
            print(f"\nNombre: {self.nombres[i]} -- Nota: {self.notas[i]}")

    def mostrar_alumnos_con_notas_mayores_o_iguales_a_7(self):
        print("\nAlumnos con notas mayores o iguales a 7\n")
        for i in range(5):
            if self.notas[i] >= 7:
                print(f"Nombre: {self.nombres[i]} -- Nota: {self.notas[i]}")

    def finalizar_programa(self):
        print("\nFin del programa")

    def mostrar_menu(self):
        while True:
            print("\nMenu")
            print("1. Cargar alumnos")
            print("2. Listar alumnos")
            print("3. Mostrar alumnos con notas mayores o iguales a 7")
            print("4. Finalizar programa")

            opcion = int(input("Ingrese su opcion: "))

            if opcion == 1:
                self.cargar_alumnos()
            elif opcion == 2:
                self.listar_alumnos()
            elif opcion == 3:
                self.mostrar_alumnos_con_notas_mayores_o_iguales_a_7()
            elif opcion == 4:
                self.finalizar_programa()
                break

agenda = Agenda()
agenda.mostrar_menu()