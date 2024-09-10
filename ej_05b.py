'''
  Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su
  suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo. 
'''

num1 = int(input('Ingresa un número: '))
num2 = int(input('Ingresa otro número: '))

if num1 > num2:
    print('SUMA:', num1 + num2)
    print('DIF:', num1 - num2)
elif num1 < num2:
    print('PROD:', num1 * num2)
    print('DIV:', num1 / num2)
else:
    print('Son IGUALES')
