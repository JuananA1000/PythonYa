'''
  Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de identificación 
  y en su valor almacenar una lista con el nombre, profesión y sueldo.
  Desarrollar las siguientes funciones:

  a) Carga de datos de empleados.

  b) Permitir modificar el sueldo de un empleado. Ingresamos su número de identificación para buscarlo.

  c) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"
'''

def modificar_sueldo(empleados):
    n_emp = int(input("Ingrese el número de identificación del empleado a modificar su sueldo: "))
    nuevo_sueldo = float(input("Ingrese el nuevo sueldo: "))
    if n_emp in empleados:
        empleados[n_emp][2] = nuevo_sueldo
    else:
        print("No se encontró el identificación ingresado")

def mostrar_analistas(empleados):
    for n_emp, datos in empleados.items():
        if datos[1] == "analista de sistemas":
            print(f"Legajo: {n_emp}, Nombre: {datos[0]}, Sueldo: {datos[2]}")

def main():
    empleados = {}
    continua = "s"

    while continua == "s":
        print(f"\nEmpleado [{len(empleados) + 1}]:")
        n_emp = int(input("ID: "))
        nombre = input("Nombre: ")
        profesion = input("Profesión: ")
        sueldo = float(input("Sueldo: "))
        empleados[n_emp] = [nombre, profesion, sueldo]
        continua = input("Desea continuar cargando datos? (s/n): ")

    mostrar_analistas(empleados)
    modificar_sueldo(empleados)
    print("\nLista de empleados actualizada:")
    for n_emp, datos in empleados.items():
        print(f"Legajo: {n_emp}, Nombre: {datos[0]}, Profesión: {datos[1]}, Sueldo: {datos[2]}")

main()
