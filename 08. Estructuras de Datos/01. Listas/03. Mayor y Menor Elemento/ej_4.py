'''
  Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si 
  dicho valor se encuentra en 2 o más posiciones en la lista)
'''

lista = []
contar_repetidos = 0

for i in range(5):
    num = int(input(f'Numero [{i+1}]: '))
    lista.append(num)

mayor = lista[0]
for i in range(1, 5):
    if lista[i] > mayor:
        mayor = lista[i]

contar_repetidos = lista.count(mayor)

print(f'\nDe esta lista: {lista}, el mayor número es: {mayor}')

if contar_repetidos > 1:
    print(f'El mayor número {mayor} se repite {contar_repetidos} veces.')
