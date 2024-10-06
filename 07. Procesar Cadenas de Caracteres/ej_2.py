'''
  Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre.
'''

nombre = 'ana'

if nombre[0] == 'a' or nombre[0] == 'e' or nombre[0] == 'i' or nombre[0] == 'o' or nombre[0] == 'u':
    print(f'{nombre} empieza por vocal')
else:
    print(f'{nombre} no empieza por vocal')
