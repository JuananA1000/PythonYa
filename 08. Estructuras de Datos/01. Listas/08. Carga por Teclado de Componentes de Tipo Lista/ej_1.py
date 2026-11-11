'''
  Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una 
  lista paralela. Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada 
  nombre y sus dos notas.
'''

nombres = []
notas = []

cuantos_alumnos = 3

for i in range(cuantos_alumnos):
    print(f'Evaluación [{i + 1}]: ')
    nombre = input(f'Nombre: ')
    not1 = int(input(f'Nota 1: '))
    not2 = int(input(f'Nota 2: '))

    nombres.append(nombre)
    notas.append([not1, not2])

print(f'\n--- Notas ---')
for i in range(cuantos_alumnos):
    print(f'{nombres[i]} --> {notas[i][0]} | {notas[i][1]}')
