'''
  Confeccionar una función de orden superior que reciba una lista que almacena valores enteros y una función con un 
  parámetro entero y que retorne un boolean.
  La función debe analizar cada elemento de la lista llamando a la función que recibe como parámetro, si retorna un True 
  se pasa a mostrar el elemento.
  En el bloque principal definir una lista de enteros.
  
  Imprimir de la lista:

  - Los valores múltiplos de 2
  - Los valores múltiplos de 3 o de 5
  - Los valores mayores o iguales a 50
  - Los valores comprendidos entre 1 y 50 o entre 70 y 100.
'''


def imprimir_si(lista, fn):
    for elemento in lista:
        if fn(elemento):
            print(elemento)


lista = [9, 20, 70, 60, 19]

print("Lista completa")
imprimir_si(lista, lambda x: True)

print("Múltiplos de 2")
imprimir_si(lista, lambda x: x % 2 == 0)

print("Múltiplos de 3 o de 5")
imprimir_si(lista, lambda x: x % 3 == 0 or x % 5 == 0)

print("Mayores o iguales a 50")
imprimir_si(lista, lambda x: x >= 50)

print("Valores [1 y 50] o [70 y 100]")
imprimir_si(lista, lambda x: x >= 1 and x <= 50 or x >= 70 and x <= 100)

