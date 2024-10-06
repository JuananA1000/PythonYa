'''
  Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
'''

lista = [10, 7, 3, 7, 2]
suma = 0

i = 0
while i < len(lista):
    suma = suma + lista[i]
    i += 1

print(
    f'La suma de todos sus elementos es: {suma}; \nAunque también puede ser {sum(lista)}')
