'''
  Definir una lista y almacenar los nombres de 3 empleados.
  Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el 
  empleado faltó.
  Imprimir los nombres de empleados y los días que faltó.
  Mostrar los empleados con la cantidad de inasistencias.
  Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.
'''

nombres = []
faltas = []
faltas_acumuladas = []

cuantos_empleados = 3

for i in range(cuantos_empleados):
    print(f'\nEmpleado [{i + 1}]: ')
    nombre = input(f'Nombre: ')
    nombres.append(nombre)

    faltas_mes = []
    for j in range(12):
        n_faltas = int(input(f'Faltas en el mes {j + 1}: '))
        faltas_mes.append(n_faltas)

    faltas.append(faltas_mes)
    faltas_acumuladas.append(sum(faltas_mes))  

print('\n--- TABLA DE ASISTENCIA ---')
for i in range(cuantos_empleados):
    print(f'\n{nombres[i]} --> {faltas_acumuladas[i]} faltas en total')

menor_faltas = min(faltas_acumuladas)
empleados_con_menos_faltas = [nombres[i] for i in range(cuantos_empleados) if faltas_acumuladas[i] == menor_faltas]

print(f'\nEl empleado con menos faltas es:')
for empleado in empleados_con_menos_faltas:
    print(f'{empleado} con {menor_faltas} faltas.')
