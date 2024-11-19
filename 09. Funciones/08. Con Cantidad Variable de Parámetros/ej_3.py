'''
  Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18 (como
  mínimo se envía un entero a la función)
'''

def return_mayores(edad, *lista_edades):
    mayores = 0

    if edad >= 18:
        mayores += 1

    for i in range(len(lista_edades)):
        if lista_edades[i] >= 18:
            mayores += 1

    return mayores

print('\nNº de Mayores de edad: ', return_mayores(34, 23, 5))
print('Nº de Mayores de edad: ', return_mayores(2, 78, 17, 8, 4))
