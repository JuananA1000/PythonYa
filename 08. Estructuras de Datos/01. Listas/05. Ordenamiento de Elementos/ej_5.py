'''
  Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor 
  a menor e imprimir nuevamente. 
'''

enteros = []

for i in range(5):
    num = int(input(f'Numerín [{i + 1}]: '))
    enteros.append(num)

print('\nLista sin ordenar: ')
print(enteros)

for h in range(4):
  for i in range(4):
    if enteros[i] > enteros[i + 1]:
        aux = enteros[i]
        enteros[i] = enteros[i + 1]
        enteros[i + 1] = aux

print('\nLista de enteros de menor a mayor')
print(enteros)

for h in range(4):
  for i in range(4):
    if enteros[i] < enteros[i + 1]:
        aux = enteros[i]
        enteros[i] = enteros[i + 1]
        enteros[i + 1] = aux

print('\nLista de enteros de mayor a menor')
print(enteros)