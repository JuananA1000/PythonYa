'''
  Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. 
  Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.

  Crear las siguientes funciones:
  a) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)

  b) Listado de todos los alumnos con sus notas

  c) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas. 
'''

def imprimir(alumnos):
    print("\nListado completo de la agenda:")
    for dni in alumnos:
        print(f"DNI: {dni} NOMBRE: {alumnos[dni][0]} APELLIDO: {alumnos[dni][1]}")

def consulta(alumnos):
    dni = input("Ingrese el DNI a consultar: ")

    if dni in alumnos:
        print(f"El dni {dni} tiene el nombre {alumnos[dni][0]} {alumnos[dni][1]}")
    else:
        print("No se encuentra el DNI")

def main():
    alumnos = {}
    continua = "s"
    i = 0

    while continua == "s":
        print(f"\nALUMNO [{i+1}]:")
        dni = input("DNI: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        alumnos[dni] = (nombre, apellido)
        continua = input("Desea cargar otro alumno[s/n]?: ")

    imprimir(alumnos)
    print("\n")
    consulta(alumnos)
    print("\n")

main()
