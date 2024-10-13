'''
  Se debe crear y cargar una sueldos donde almacenar 5 sueldos. Ordenar de menor a mayor los sueldos.
'''

sueldos = []

for i in range(5):
    sueldo = int(input(f'Ingrese sueldo [{i + 1}]: '))
    sueldos.append(sueldo)

print('\nLista sin ordenar: ')
print(sueldos)

for h in range(4):
  for i in range(4):
    if sueldos[i] > sueldos[i + 1]:
        aux = sueldos[i]
        sueldos[i] = sueldos[i + 1]
        sueldos[i + 1] = aux

print('\nLista de sueldos de menor a mayor')
print(sueldos)
