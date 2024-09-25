'''
  Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor.
'''

num1 = int(input('Ingresa un número: '))
num2 = int(input('Ingresa otro número: '))
num3 = int(input('Ingresa un tercer número: '))

if num1 > num2 and num1 > num3:
    # Formateo para números enteros
    print('El %d es el mayor' % (num1))
elif num2 > num1 and num2 > num3:
    print('El %d es el mayor' % (num2))
else:
    print('El %d es el mayor' % (num3))
