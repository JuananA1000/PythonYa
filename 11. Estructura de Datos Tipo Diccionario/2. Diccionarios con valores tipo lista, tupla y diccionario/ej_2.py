'''
  Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. Permitir almacenar distintas actividades 
  para la misma fecha (se ingresa la hora y la actividad).

  Implementar las siguientes funciones:
  a) Carga de datos en la agenda.

  b) Listado completo de la agenda.

  c) Consulta de una fecha.
'''

def imprimir(agenda):
    print("\nListado completo de la agenda:")
    for fecha in agenda:
        print(f"FECHA: {fecha} HORA: {agenda[fecha][0]} ACTIVIDAD: {agenda[fecha][1]}")

def consulta(agenda):
    fecha = input("Ingrese la fecha a consultar: ")
    if fecha in agenda:
        print(f"FECHA: {fecha} HORA: {agenda[fecha][0]} ACTIVIDAD: {agenda[fecha][1]}")
    else:
        print("Fecha no encontrada")

def main():
    agenda = {}
    continua = "s"
    i = 0

    while continua == "s":
        print(f"\nACTIVIDAD [{i+1}]:")
        fecha = input("Fecha: ")
        hora = input("Hora: ")
        actividad = input("Descripción: ")
        agenda[fecha] = (hora, actividad)
        continua = input("Desea cargar otra actividad[s/n]?: ")

    imprimir(agenda)
    print("\n")
    consulta(agenda)
    print("\n")

main()
