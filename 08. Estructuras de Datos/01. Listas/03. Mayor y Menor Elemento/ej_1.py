'''
  Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.
'''

lista = []

for i in range(5):
    num = int(input(f'Numero [{i+1}]: '))
    lista.append(num)

# Consideramos al primero como el mayor
mayor = lista[0]
for i in range(1, 5):
    if lista[i] > mayor:
        mayor = lista[i]

print(f'\nDe esta lista: {lista}, el mayor número es: {mayor}')
