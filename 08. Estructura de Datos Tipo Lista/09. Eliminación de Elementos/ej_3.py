'''
  Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada
  empleado.
  Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
  Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
'''

empleados = []
sueldos = []

cuantos_empleados = int(input('Cuántos empleados: '))
for i in range(cuantos_empleados):
    print(f'Empleado [{i+1}]: ')
    nom = input('Nombre: ')
    sue = float(input('Sueldo: '))

    empleados.append(nom)
    sueldos.append(sue)

print('\n--- TABLA DE SUELDOS ---')
for i in range(len(sueldos)):
    print(f'Nombre: {empleados[i]} | Sueldo: {sueldos[i]}€')

i = 0
while i < len(sueldos):
    if sueldos[i] > 10000:
        empleados.pop(i)
        sueldos.pop(i)
    else:
        i += 1

print('\n--- EMPLEADOS DE MENOS DE 10000€ ---')
for i in range(len(sueldos)):
    print(f'Nombre: {empleados[i]} | Sueldo: {sueldos[i]:.2f}€')
