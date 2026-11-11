'''
  Otro problema típico que se presenta para analizar la recursividad es el obtener el factorial de un número.
  Recordar que el factorial de un número es el resultado que se obtiene de multiplicar dicho número por el anterior y 
  así sucesivamente hasta llegar a uno.

  Ej. el factorial de 4 es 4 * 3 * 2 * 1 es decir 24. 
'''

def factorial(fact):
    if fact > 0:
        valor = fact * factorial(fact - 1)
        return valor
    else:
        return 1


print(f"El factorial de {4} es {factorial(4)}")
