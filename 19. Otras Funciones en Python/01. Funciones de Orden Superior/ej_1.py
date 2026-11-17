'''
  Definir una función de orden superior llamada operar. Llegan como parámetro dos enteros y una función. En el bloque de 
  la función llamar a la función que llega como parámetro y enviar los dos primeros parámetros.
  
  La función retorna un entero.
'''


def operar(v1, v2, fn):
    return fn(v1, v2)


def sumar(x1, x2):
    return x1+x2


def restar(x1, x2):
    return x1-x2


def multiplicar(x1, x2):
    return x1*x2


def dividir(x1, x2):
    return x1/x2


suma = operar(10, 3, sumar)
resta = operar(10, 3, restar)
multip = operar(30, 10, multiplicar)
divi = operar(10, 2, dividir)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multip}")
print(f"División: {divi}")
