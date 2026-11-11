'''
  Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número 
  entero 5.
'''

lista = []

for i in range(10):
    num = int(input(f'Número [{i+1}]: '))
    lista.append(num)

print('\nLista creada: ', lista)

i = 0
while i < len(lista):
    if lista[i] == 5:
        lista.pop(i)
    else:
        i = i+1

print('\nLista final: ', lista)
