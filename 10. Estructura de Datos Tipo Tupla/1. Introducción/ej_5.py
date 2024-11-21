'''
  Confeccionar un programa con las siguientes funciones:
  
  a) Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores

  b) Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados y muestre el nombre del 
  empleado con sueldo mayor.

  En el bloque principal del programa llamar dos veces a la función de carga y seguidamente llamar a la función que 
  muestra el nombre de empleado con sueldo mayor.
'''

def cargar_empleado():
    nombre = input('Nombre: ')
    sueldo = int(input('Sueldo: '))

    return (nombre, sueldo)

def mayor_sueldo(emp1, emp2):
    if emp1[1] > emp2[1]:
        print(f'\n{emp1[0]} tiene el mayor sueldo, con {emp1[1]}€')
    else:
        print(f'\n{emp2[0]} tiene el mayor sueldo, con {emp2[1]}€')

# bloque principal
empleado1 = cargar_empleado()
empleado2 = cargar_empleado()
mayor_sueldo(empleado1, empleado2)
