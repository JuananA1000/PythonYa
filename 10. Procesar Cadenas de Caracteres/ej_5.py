'''
  Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio 
  en blanco es igual a " ", en cambio una cadena vacía es ""
'''

oracion = 'Tengo una muñeca vestida de punk, con su chupa de cuero y su cresta azul.'

cuenta_espacios = 0

i = 1
while i < len(oracion):
    if oracion[i] == ' ':
        cuenta_espacios += 1
    i += 1

print(f'La frase tiene {cuenta_espacios} espacios')
