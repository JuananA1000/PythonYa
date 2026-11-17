'''
  Definir una función de orden superior llamada operar. Llegan como parámetro dos enteros y una función. En el bloque de 
  la función llamar a la función que llega como parámetro y enviar los dos primeros parámetros.
  
  Desde el bloque principal llamar a operar y enviar distintas expresiones lambdas que permitan sumar, restar, 
  multiplicar y dividir 
'''


def operar(v1, v2, fn):
    return fn(v1, v2)


suma = operar(10, 3, lambda x1, x2: x1+x2)
resta = operar(10, 3, lambda x1, x2: x1-x2)
multip = operar(30, 10, lambda x1, x2: x1*x2)
divis = operar(10, 2, lambda x1, x2: x1/x2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multip}")
print(f"División: {divis}")
