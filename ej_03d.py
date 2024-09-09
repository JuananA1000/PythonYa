'''
  Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.
'''

num1 = int(input('Introduce número 1: '))
num2 = int(input('Introduce número 2: '))
num3 = int(input('Introduce número 3: '))
num4 = int(input('Introduce número 4: '))

print('SUMA: ', sum(num1, num2, num3, num4))
print('PROMEDIO: ', sum(num1, num2, num3, num4) / len())
