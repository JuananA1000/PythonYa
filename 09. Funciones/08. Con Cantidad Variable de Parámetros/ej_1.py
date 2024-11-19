'''
  Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros, retornar la suma de 
  dichos parámetros.
'''

def sumar(num1, num2, *lista):
    suma = num1 + num2

    for x in range(len(lista)):
        suma = suma + lista[x]

    return suma

print('\nResultado = ', sumar(34, 5))
print('\nResultado = ', sumar(2, 5, 7, 8, 4))
