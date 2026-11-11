'''
  Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento debe ser una lista de 5 enteros.
  Calcular y mostrar la suma de cada lista contenida en la lista principal.
'''

lista = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]]

for i in range(len(lista)):
    sum1 = 0
    sum2 = 0
    for j in range(len(lista[i])):
        sum1 += lista[0][j]
        sum2 += lista[1][j]

print('Suma primera lista: ', sum1)
print('Suma segunda lista: ', sum2)
