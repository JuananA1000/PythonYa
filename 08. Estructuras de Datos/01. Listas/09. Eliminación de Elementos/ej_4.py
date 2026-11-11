'''
  Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva
  lista con dichos valores.
'''

numeros = []
cuantos_numeros = 5

for i in range(cuantos_numeros):
    num = int(input(f'Número [{i+1}]: '))

    numeros.append(num)

print('\n--- NÚMEROS ---')
for i in range(len(numeros)):
    print(f' {numeros[i]} ', end='')

i = 0
while i < len(numeros):
    if numeros[i] >= 10:
        numeros.pop(i)
    else:
        i += 1

print('\n\n--- NÚMEROS MENORES A DIEZ ---')
for i in range(len(numeros)):
    print(f' {numeros[i]} ', end='')
