'''
  Confeccionar una función de orden superior que reciba un String y una función con un parámetro de tipo String que 
  retorna un Boolean.
  La función debe analizar cada elemento del String llamando a la función que recibe como parámetro, si retorna un True 
  se agrega dicho caracter al String que se retornará.
  En el bloque principal definir un String con una cadena cualquiera.
  Llamar a la función de orden superior y pasar expresiones lambdas para filtrar y generar otro String con las 
  siguientes restricciones:

  - Un String solo con las vocales
  - Un String solo con los caracteres en minúsculas
  - Un String con todos los caracteres no alfabéticos
'''


def filtrar(cadena, fn):
    cad = ""
    for caracter in cadena:
        if fn(caracter):
            cad = cad+caracter
    return cad


cadena = "¿Esto es la prueba 1 o la prueba 2?"
print("String original")
print(cadena)

print("String solo con las vocales")
cadena2 = filtrar(cadena, lambda car: car == 'a' or car == 'e' or car == 'i' or car == 'o' or car == 'u'
                  or car == 'A' or car == 'E' or car == 'I' or car == 'O' or car == 'U')
print(cadena2)

print("String solo con los caracteres en minúscula")
cadena3 = filtrar(cadena, lambda car: car >= 'a' and car <= 'z')
print(cadena3)

print("String solo con los caracteres no alfabéticos")
cadena3 = filtrar(cadena, lambda car: not (car >= 'a' and car <= 'z') and not (car >= 'A' and car <= 'Z'))
print(cadena3)
