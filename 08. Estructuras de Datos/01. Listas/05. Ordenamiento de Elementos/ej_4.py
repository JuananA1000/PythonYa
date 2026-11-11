'''
  Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos de 
  dichos empleados. Imprimir la lista de sueldos ordenados de menor a mayor. 
'''

numero_empleados = int(input('Cantidad de Empleados: '))
sueldos = []

for i in range(numero_empleados):
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
