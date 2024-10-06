'''
  Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores 
  a 7. 
'''

lista = [3, 5, 10, 8, 9]
cuantos_valores = 0

i = 0
while i < len(lista):
    if lista[i] >= 7:
        cuantos_valores += 1
    i += 1

print(f'Hay {cuantos_valores} números mayores a 7')
