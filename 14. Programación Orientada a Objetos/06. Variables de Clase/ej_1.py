'''
  Definir una clase Cliente que almacene un código de cliente y un nombre.
  En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que tienen suspendidas 
  sus cuentas corrientes.
  Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.
'''

class Cliente:
    suspendidos = []

    def __init__(self, cod_cliente, nom_cliente):
        self.cod_cliente = cod_cliente
        self.nom_cliente = nom_cliente

    def imprimir(self):
        print("Codigo:", self.cod_cliente)
        print("Nombre:", self.nom_cliente)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.cod_cliente in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("_____________________________")

    def suspender(self):
        Cliente.suspendidos.append(self.cod_cliente)


cliente1 = Cliente(1, "Juan")
cliente2 = Cliente(2, "Ana")
cliente3 = Cliente(3, "Diego")
cliente4 = Cliente(4, "Pedro")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)
