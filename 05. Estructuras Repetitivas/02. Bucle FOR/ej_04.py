'''
  Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los
  valores ingresados y su promedio. Este problema ya lo desarrollamos, lo resolveremos empleando la estructura for para
  repetir la carga de los diez valores por teclado.
'''
cuantos_valores = 10
suma = 0

for i in range(cuantos_valores):
    num = int(input('Numerín [%d]: ' % i))
    suma += num

promedio = suma / cuantos_valores

print('\nSuma: ', suma)
print('Promedio: ', promedio)
