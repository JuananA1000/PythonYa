'''
  Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
  Debe mostrar un menú con las siguientes opciones:

  a) Carga de un contacto en la agenda.

  b) Listado completo de la agenda.

  c) Consulta ingresando el nombre de la persona.

  d) Modificación de su teléfono y mail.

  e) Finalizar programa.
'''

class Agenda:
    def __init__(self):
        self.nombres = []
        self.telefonos = []
        self.mails = []

    def cargar_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        mail = input("Mail: ")

        self.nombres.append(nombre)
        self.telefonos.append(telefono)
        self.mails.append(mail)

    def listar_contactos(self):
        print("\nContactos")
        for i in range(len(self.nombres)):
            print(f"\nNombre: {self.nombres[i]} -- Telefono: {self.telefonos[i]} -- Mail: {self.mails[i]}")

    def mostrar_contacto(self):
        nombre = input("Nombre: ")
        for i in range(len(self.nombres)):
            if self.nombres[i] == nombre:
                print(f"\nNombre: {self.nombres[i]} -- Telefono: {self.telefonos[i]} -- Mail: {self.mails[i]}")
                break

    def finalizar_programa(self):
        print("\nFin del programa")

    def mostrar_menu(self):
        while True:
            print("\nMenu")
            print("1. Cargar contacto")
            print("2. Listar contactos")
            print("3. Mostrar contacto")
            print("4. Finalizar programa")

            opcion = int(input("Ingrese su opcion: "))

            if opcion == 1:
                self.cargar_contacto()
            elif opcion == 2:
                self.listar_contactos()
            elif opcion == 3:
                self.mostrar_contacto()
            elif opcion == 4:
                self.finalizar_programa()
                break

agenda = Agenda()
agenda.mostrar_menu()
