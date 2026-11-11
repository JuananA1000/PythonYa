'''
  Implementación de una función recursiva que reciba un parámetro de tipo entero y luego llame en forma recursiva con el 
  valor del parámetro menos 1.
'''

def imprimir_descendente(n):
    if n > 0:
        print(n)
        imprimir_descendente(n - 1)

imprimir_descendente(5)