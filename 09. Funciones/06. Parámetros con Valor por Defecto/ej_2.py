'''
  Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores. Debe 
  tener tres parámetros por defecto. 
'''

def suma_parametros_por_defecto(num1, num2, num3=4, num4=3, num5=7):
    suma = num1 + num2 + num3 + num4 + num5
    return suma

print(suma_parametros_por_defecto(3, 5))  # Imprime 22
print(suma_parametros_por_defecto(3, 5, 7, 7, 2))  # Imprime 24
