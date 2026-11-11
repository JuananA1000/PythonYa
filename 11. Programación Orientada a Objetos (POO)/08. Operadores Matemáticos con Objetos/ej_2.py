'''
  Desarrollar una clase llamada Lista, que permita pasar al método __init__ una lista de valores enteros.
  Redefinir los operadores +, -, * y // con respecto a un valor entero. 
'''

class Lista:
    def __init__(self, lista):
        self.lista = lista

    def __add__(self, otro):
        li = []
        for i in range(len(self.lista)):
            li.append(self.lista[i] + otro.lista[i])
        return li

    def __sub__(self, otro):
        li = []
        for i in range(len(self.lista)):
            li.append(self.lista[i] - otro.lista[i])
        return li

    def __mul__(self, otro):
        li = []
        for i in range(len(self.lista)):
            li.append(self.lista[i] * otro.lista[i])
        return li

    def __floordiv__(self, otro):
        li = []
        for i in range(len(self.lista)):
            li.append(self.lista[i] // otro.lista[i])
        return li

    # Utilizamos __str__ para evitar que el resultado salga así: <__main__.Lista object at 0x000001E916DC3FD0> + <__main__.Lista object at 0x000001E916DC3EB0> = [5, 7, 9]
    def __str__(self):
        return str(self.lista)


l1 = Lista([1, 2, 3])
l2 = Lista([4, 5, 6])

print(f"\n{l1} + {l2} = {l1 + l2}")
print(f"{l1} - {l2} = {l1 - l2}")
print(f"{l1} * {l2} = {l1 * l2}")
print(f"{l1} // {l2} = {l1 // l2}")
