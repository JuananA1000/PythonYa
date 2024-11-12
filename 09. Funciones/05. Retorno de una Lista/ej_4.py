'''
  En una empresa se almacenaron los sueldos de 10 personas.
  Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
  
  a) Carga de los sueldos en una lista.
  
  b) Impresión de todos los sueldos.
  
  c) Cuántos tienen un sueldo superior a $4000.
  
  d) Retornar el promedio de los sueldos.
  
  e) Mostrar todos los sueldos que están por debajo del promedio. 
'''

def return_sueldos(li_nom, li_su):
    return li_nom, li_su

def return_menores_a_4000(li_nom, li_su):
    mayores = []

    for i in range(len(li_su)):
        if li_su[i] < 4000:
            mayores.append(li_nom[i])

    return mayores

def return_promedio_sueldos(li_su):
    prom = sum(li_su) / len(li_su)

    return prom

def main():
    nombres = []
    sueldos = []
    cuantos_empleados = 10

    for i in range(cuantos_empleados):
        print(f'\nPersona {i + 1}')
        nombre = input('Nombre: ')
        sueldo = int(input('Sueldo: '))

        nombres.append(nombre)
        sueldos.append(sueldo)

    res_nombres,  res_sueldos = return_sueldos(nombres, sueldos)
    mayores = return_menores_a_4000(nombres, sueldos)
    promedio = return_promedio_sueldos(sueldos)

    print('\nSUELDOS POR EMPLEADO')
    for i in range(cuantos_empleados):
        print(f'Nombre: {res_nombres[i]} | Sueldo: {res_sueldos[i]}')

    print('\nEMPLEADOS CON SUELDO < 4000:', end=' ')
    for nombre in mayores:
        print(nombre, end=' ')

    print(f'\n\nEl sueldo promedio es: {promedio:.2f}$')

main()
