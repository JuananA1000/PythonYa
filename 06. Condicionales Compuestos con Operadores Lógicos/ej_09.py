'''
  Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule y muestre el mayor y el 
  menor de ellos) 
'''

num1 = int(input('Ingresa un número de num1: '))
num2 = int(input('Ingresa un número de num2: '))
num3 = int(input('Ingresa un número de num3: '))

# Mostrar el MENOR
if num1 < num2 and num1 < num3:
    print('El MENOR es: %d' % (num1))
else:
    if num2 < num3:
        print('El MENOR es: %d' % (num2))
    else:
        print('El MENOR es: %d' % (num3))

# Mostrar el MAYOR
if num1 > num2 and num1 > num3:
    print('El MAYOR es: %d' % (num1))
else:
    if num2 > num3:
        print('El MAYOR es: %d' % (num2))
    else:
        print('El MAYOR es: %d' % (num3))
