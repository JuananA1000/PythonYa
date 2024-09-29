'''
  Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y
  cuántos impares.
  Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de
  dos valores, por ejemplo 11%2 retorna un 1):

  if valor % 2 == 0:
'''
cuantos_numeros = int(input('Cuántos números: '))
cuenta_pares = 0
cuenta_impares = 0

i = 1
while i <= cuantos_numeros:
    num = int(input('Introduce número [%d]: ' % i))
    i += 1

    if num % 2 == 0:
        cuenta_pares += 1
    else:
        cuenta_impares += 1

print('\nPARES: %d' % cuenta_pares)
print('IMPARES: %d' % cuenta_impares)
