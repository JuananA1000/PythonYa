'''
  Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, imprimir en pantalla la
  leyenda "Alguno de los números es menor a diez". 
'''

num1 = int(input('Ingresa un número de num1: '))
num2 = int(input('Ingresa un número de num2: '))
num3 = int(input('Ingresa un número de num3: '))

if num1 < 10 or num2 < 10 or num3 < 10:
    print('Alguno de los números es MENOR a diez')
else:
    print('Alguno de los números es MAYOR a diez')
