'''
  Definir una lista con 5 valores enteros, luego a partir de la primer lista generar una segunda lista con los valores 
  elevados al cuadrado.
'''

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [i**2 for i in lista_1]

print(f"Lista 1: {lista_1}")
print(f"Lista 2: {lista_2}")