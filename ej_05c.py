'''
   Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".
'''

nota1 = int(input('Ingresa nota 1: '))
nota2 = int(input('Ingresa nota 2: '))
nota3 = int(input('Ingresa nota 3: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('Media: ', media, 'LA PROMOSIÓ')
elif media < 7:
    print('Media: ', media, 'no hay promosió')