'''
  Se debe crear y cargar una sueldos donde almacenar 5 sueldos. Desplazar el sueldo mayor de la sueldos a la última posición.
'''

sueldos = []

for i in range(5):
    sueldo = int(input(f'Ingrese sueldo [{i + 1}]: '))
    sueldos.append(sueldo)

print('\nLista sin ordenar: ')
print(sueldos)

for i in range(4):
    if sueldos[i] > sueldos[i + 1]:
        aux = sueldos[i]
        sueldos[i] = sueldos[i + 1]
        sueldos[i + 1] = aux

print('\nLista con el último elemento ordenado')
print(sueldos)
