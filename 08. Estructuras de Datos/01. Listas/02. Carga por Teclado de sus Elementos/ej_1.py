'''
  Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista 
  generada.
'''

lista = []

for i in range(5):
    num = int(input(f'Añade número {i+1}: '))
    lista.append(num)

print(f'Aquí tienes tu lista: {lista}')
