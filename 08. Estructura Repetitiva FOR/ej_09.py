'''
  Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.
'''

suma = 0

for i in range(10):
    num = int(input('Numerín [%d]: ' % i))

    if i >= 5 and i:
        suma += num

print('\nSuma: ', suma)
