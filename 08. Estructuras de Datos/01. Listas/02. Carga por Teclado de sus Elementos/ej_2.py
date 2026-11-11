'''
  Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar
  el cero. Mostrar finalmente el tamaño de la lista.
'''

lista = []

num = int(input(f'Añade número 1: '))
i = 1
while num != 0:
    lista.append(num)
    num = int(input(f'Añade número {i+1}: '))

print(f'Aquí tienes tu lista: {lista}')
