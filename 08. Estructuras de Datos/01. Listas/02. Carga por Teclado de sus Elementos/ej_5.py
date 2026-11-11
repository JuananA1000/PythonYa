'''
  Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde).
  Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
  Imprimir las dos listas de sueldos.
'''

sueldos_mñn =[]
sueldos_trd =[]

print("--- Turno de MAÑANA ---:")
for i in range(4):
    sueldo = float(input(f"Sueldo del empleado {i + 1}: "))
    sueldos_mñn.append(sueldo)

print("--- Turno de TARDE ---:")
for i in range(4):
    sueldo = float(input(f"Sueldo del empleado {i + 1}: "))
    sueldos_trd.append(sueldo)

print("\nSueldos del turno de la mañana:", sueldos_mñn)
print("Sueldos del turno de la tarde:", sueldos_trd)