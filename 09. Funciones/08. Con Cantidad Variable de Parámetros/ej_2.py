'''
  Desempaquetar una lista o tupla.
  Puede ser que tengamos una función que recibe una cantidad fija de parámetros y necesitemos llamarla enviando valores 
  que se encuentran en una lista o tupla. La forma más sencilla es anteceder el caracter * al nombre de la variable:
'''

def sumar(num1, num2, num3):
    return num1 + num2 + num3

print('\nResultado: ', sumar(1, 2, 3))

lista = [12, 23, 34]
suma = sumar(*lista)
print('\nResultado desempaquetado: ', suma)