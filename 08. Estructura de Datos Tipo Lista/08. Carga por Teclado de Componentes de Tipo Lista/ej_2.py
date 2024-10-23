'''
  Se tiene que cargar la siguiente información:
  - Nombres de 3 empleados
  - Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
  Confeccionar el programa para:

  a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
  
  b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
  
  c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
  
  d) Obtener el nombre del empleado que tuvo el mayor_sueldo ingreso acumulado
'''

nombres = []
sueldos = []
ingreso_acumulado = []

cuantos_empleados = 3

for i in range(cuantos_empleados):
    print(f'\nCurrante [{i + 1}]: ')
    nombre = input(f'Nombre: ')
    sue1 = int(input(f'Sueldo 1: '))
    sue2 = int(input(f'Sueldo 2: '))
    sue3 = int(input(f'Sueldo 3: '))

    nombres.append(nombre)
    sueldos.append([sue1, sue2, sue3])

for i in range(cuantos_empleados):
    total = sueldos[i][0] + sueldos[i][1] + sueldos[i][2]
    ingreso_acumulado.append(total)

print('\n --- TABLA DE SUELDOS ---')
for i in range(cuantos_empleados):
    print(
        f'\n{nombres[i]} --> {sueldos[i][0]} | {sueldos[i][1]} | {sueldos[i][2]} Acumulado: {ingreso_acumulado[i]}')

pos_mayor = 0
mayor_sueldo = ingreso_acumulado[0]
for i in range(3):
    if ingreso_acumulado[i] > mayor_sueldo:
        mayor_sueldo = ingreso_acumulado[i]
        pos_mayor = i

print(f'\nEl empleado con más ingresos ha sido {nombres[pos_mayor]} con {mayor_sueldo}€')
