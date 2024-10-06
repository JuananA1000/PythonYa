'''
  Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de ellos.
'''

num1 = int(input('Ingresa un número: '))
num2 = int(input('Ingresa otro número: '))

if num1 > num2:
    print('El numero 1:', num1, 'es MAYOR que el 2:', num2)
elif num1 < num2:
    print('El numero 1:', num1, 'es MENOR que el 2:', num2)
else:
    print('Son IGUALES')
