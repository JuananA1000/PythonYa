'''
  Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos. 
'''

num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))

if num1 != num2 and num2 != num3 and num1 != num3:
    if num1 > num2 and num1 > num3:
        print(f'{num1} es el número mayor')
    elif num2 > num1 and num2 > num3:
        print(f'{num2} es el número mayor')
    else:
        print(f'{num3} es el número mayor')
else:
    print('Hay algun número repetido')
