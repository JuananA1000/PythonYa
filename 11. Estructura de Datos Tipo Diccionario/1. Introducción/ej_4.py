'''
  Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con 
  su nombre.
  
  Desarrollar las siguientes funciones:
  a) Cargar por teclado los datos de 4 personas.
  
  b) Listado completo del diccionario.
  
  c) Consulta del nombre de una persona ingresando su número de documento. 
'''


def imprimir(diccionario):
    print("\nDICCIONARIO")

    for dni in diccionario:
        print(f'{dni}: {diccionario[dni]}')


def consulta_nombre(diccionario):
    dni = input("\nIngrese el DNI a consultar: ")

    if dni in diccionario:
        print(f"El dni {dni} tiene el nombre {diccionario[dni]}")
    else:
        print("No se encuentra el DNI")

def main():
    diccionario = {}

    for i in range(2):
        print(f"\nPersona [{i+1}]")
        dni = input("DNI: ")
        nombre = input("Nombre: ")
        diccionario[dni] = nombre

    return diccionario

diccionario = main()
imprimir(diccionario)
consulta_nombre(diccionario)
