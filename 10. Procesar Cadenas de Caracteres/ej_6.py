'''
  Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. Crear 
  un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es 
  una vocal.
'''

oracion = 'MerkelPuta'
oracion_min = oracion.lower()

cuenta_vocales = 0

i = 0
while i < len(oracion_min):
    if oracion_min[i] == 'a' or oracion_min[i] == 'e' or oracion_min[i] == 'i' or oracion_min[i] == 'o' or oracion_min[i] == 'u':
        cuenta_vocales += 1

    i += 1

print(f'La frase tiene {cuenta_vocales} vocales')
