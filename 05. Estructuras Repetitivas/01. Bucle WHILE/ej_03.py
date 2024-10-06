'''
  Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los
  valores ingresados y su promedio.
'''

suma = 0

x = 1
while x <= 3:
    num = int(input('Ingresa un número: '))
    suma = suma + num
    x += 1

promedio = suma / 3

print('Suma: %d' % suma)
print('Promedio: %d' % promedio)
