'''
  Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la 
  lista y la posición donde se encuentra.
'''

lista = []

for i in range(5):
    num = int(input(f'Numero [{i+1}]: '))
    lista.append(num)

menor = lista[0]
for i in range(1, 5):
    if lista[i] < menor:
        menor = lista[i]

print(
    f'\nDe esta lista: {lista}, el menor número es: {menor}, y su posicion es: [{i}]')
