'''
  Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos 
  mensajes:

  Si el promedio es >=7 mostrar "Promocionado".
  Si el promedio es >=4 y <7 mostrar "Regular".
  Si el promedio es <4 mostrar "Suspenso". 
'''

nota1 = int(input('Ingresa nota 1: '))
nota2 = int(input('Ingresa nota 2: '))
nota3 = int(input('Ingresa nota 3: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('Media: ', media, 'LA PROMOSIÓ')
elif media >= 4 and media < 7:
    print('Media: ', media, 'Regular')
elif media < 4:
    print('Media: ', media, 'no hay promosió')
