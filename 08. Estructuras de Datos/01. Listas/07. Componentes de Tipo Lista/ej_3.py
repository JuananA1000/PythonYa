'''
  Crear una lista por asignación. La lista tiene que tener 5 elementos. Cada elemento debe ser una lista, la primera 
  lista tiene que tener un elemento, la segunda dos elementos, la tercera tres elementos y así sucesivamente.
  Sumar todos los valores de las listas.
'''

lista = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
suma_total = 0

for i in range(len(lista)):
    suma_grupo = 0  # Resetear la suma del grupo para cada nueva sublista

    for j in range(len(lista[i])):
        suma_grupo += lista[i][j]
        suma_total += lista[i][j]

    print(f'Suma grupo [{i+1}]: ', suma_grupo)

print('\nSuma total: ', suma_total)
