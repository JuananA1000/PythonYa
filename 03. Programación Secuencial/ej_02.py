'''
  Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor
  entero en el precio del producto)
'''

precio = int(input('Introduce el precio de producto: '))
cantidad = int(input('Introduce la cantidad de producto: '))

total = precio * cantidad

print('TOTAL: ', total)
