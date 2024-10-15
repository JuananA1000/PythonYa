'''
  Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 
  enteros.
  Imprimir sus elementos accediendo de diferentes modos.
'''

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print('\nLista completa')
print(lista)

print('\nImprimir un grupo de la lista')
print(lista[0]) # El número puede ser cualquiera segun la cantidad de grupos en la lista

print('\nImprimir un componente de un grupo de la lista')
print(lista[0][1])

print('\nLista contenida en un componente')
for i in range(len(lista[0])):
    print(lista[0][i], end='')

print('Imprimimos cada elemento de cada una de las listas contenidas en la lista principal')
for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(lista[i][j], end='')
