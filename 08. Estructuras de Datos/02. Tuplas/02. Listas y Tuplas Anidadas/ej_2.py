'''
  Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del empleado junto a sus
  últimos tres sueldos (estos tres valores en una tupla)
  El programa debe tener las siguientes funciones:

  a) Carga de los nombres de empleados y sus últimos tres sueldos.

  b) Imprimir el monto total cobrado por cada empleado.

  c) Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.

  Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
  
  empleados = [["juan", (2000, 3000, 4233)], ["ana", (3444, 1000, 5333)], etc.]
'''

def return_sueldo_por_empleado(li_emp):
    resultados = []
  
    for empleado in li_emp:
        nombre, sueldos = empleado
        total = sum(sueldos)
        resultados.append((nombre, total))  
  
    return resultados

def return_mayores_a_10000(li_emp):
    resultados = []
  
    for empleado in li_emp:
        nombre, sueldos = empleado
        if sum(sueldos) > 10000:
            resultados.append(nombre)  
  
    return resultados

def main():
    empleados = []  
    cuantos_empleados = 5

    for i in range(cuantos_empleados):
        print(f'\n-- EMPLEADO {i + 1} --')
        nombre = input('Nombre: ')
        sueldos = [] # Atención a esto: creamos una LISTA de sueldos...

        for j in range(3):
            sueldo = int(input(f'Sueldo {j + 1}: '))
            sueldos.append(sueldo)

        empleados.append([nombre, tuple(sueldos)]) # ...y luego la pasamos a TUPLA, que es la estructura que buscamos  

    sueldo_por_empleado = return_sueldo_por_empleado(empleados)
    mayores_a_10000 = return_mayores_a_10000(empleados)

    print('\nSueldos totales por empleado:')
    for nombre, total in sueldo_por_empleado:
        print(f'{nombre}: {total}')

    print('\nEmpleados con ingresos mayores a 10000: ', end='')
    for nombre in mayores_a_10000:
        print(nombre, end=' ')

main()
