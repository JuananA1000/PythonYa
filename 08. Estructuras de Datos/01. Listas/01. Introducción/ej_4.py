'''
  Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior 
  a 100. 
'''

lista = [34, 56, 100, 123, 456, 76, 78, 67]
cuantos_valores = 0

i = 0
while i < len(lista):
    if lista[i] > 100:
        cuantos_valores += 1
    i += 1

print(f'Hay {cuantos_valores} números mayores a 100')
