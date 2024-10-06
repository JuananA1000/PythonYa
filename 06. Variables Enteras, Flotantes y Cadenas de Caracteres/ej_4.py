'''
  Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados en forma alfabética.
'''

nom1 = input('Nombre 1: ')
nom2 = input('Nombre 2: ')

if nom1 < nom2:
    print(f'{nom1}, {nom2}')
else:
    print(f'{nom2}, {nom1}')
