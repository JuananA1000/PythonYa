'''
  Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este
  resultado se lo multiplica por el tercero. 
'''

num1 = int(input('Ingresa un número de num1: '))
num2 = int(input('Ingresa un número de num2: '))
num3 = int(input('Ingresa un número de num3: '))

resultado = ((num1 + num3) * num3)

if num1 == num2 and num1 == num3 and num2 == num3:
    print('El resultado es: %d' % (resultado))
else:
    print('POLLA')
