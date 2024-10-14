'''
  Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. Luego ordenar las notas
  de mayor a menor. Imprimir las notas y los nombres de los alumnos.

  Debe quedar claro que cuando intercambiamos las notas para dejarlas ordenadas de mayor a menor debemos intercambiar
  los nombres para que las listas continúen paralelas (es decir que en los mismos subíndices de cada lista continúe la
  información relacionada)
'''

nombres = []
notas = []

for i in range(5):
    print(f'Evaluación [{i + 1}]: ')
    nombre = input(f'Nombre [{i + 1}]: ')
    nota = int(input(f'Nota [{i + 1}]: '))

    nombres.append(nombre)
    notas.append(nota)

print(f'\n--- Notas ---')
for i in range(5):
    print(f'{nombres[i]} --> {notas[i]}')

for h in range(4):
    for i in range(4):
        if notas[i] < notas[i + 1]:
            aux_not = notas[i]
            aux_nom = nombres[i]

            notas[i] = notas[i + 1]
            notas[i + 1] = aux_not

            nombres[i] = nombres[i + 1]
            nombres[i + 1] = aux_nom

print('\n--- Notas de menor a mayor ---')
for i in range(5):
    print(f'{nombres[i]} --> {notas[i]}')
