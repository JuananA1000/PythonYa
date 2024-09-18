'''
  Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es
  decir, cero)
'''

numero = int(input('Número: '))

if numero > 0:
    print(f'{numero} es POSITIVO')
elif numero < 0:
    print(f'{numero} es NEGATIVO')
else:
    print(f'{numero} es el NULO')
