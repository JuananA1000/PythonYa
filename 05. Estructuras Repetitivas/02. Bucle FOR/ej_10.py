'''
  Desarrollar un programa que muestre las tablas de multiplicar
'''

tabla = int(input('Número de Tabla: '))

for i in range(11):
    if i > 0:
        prod = tabla * i

        print('%d x %d = %d' % (tabla, i, prod))
