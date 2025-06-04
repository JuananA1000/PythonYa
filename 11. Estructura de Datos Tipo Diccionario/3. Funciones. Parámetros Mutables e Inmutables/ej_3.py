'''
  Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor su número
  telefónico:
  a) Carga de contactos y su número telefónico.

  b) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.

  c) Imprimir la lista completa de contactos con sus números telefónicos.
'''

def modificar_contacto(lista):
    nombre = input("Ingrese el nombre del contacto que desea modificar: ")

    for i in range(len(lista)):
        if lista[i]["Contacto"] == nombre:
            lista[i]["Tlf"] = input("Ingrese el nuevo número telefónico: ")
            break

    return lista

def main():
    lista = []
    continua = "s"
    i = 1

    while continua == "s":
        print(f"\nContacto [{i}]")
        nom = input("Nombre: ")
        tlf = input("Tlf: ")
        lista.append({"Contacto": nom, "Tlf": tlf})
        continua = input("Desea continuar[s/n]?: ")
        i += 1

    print(f"\nLista completa: {lista}")
    modificar_contacto(lista)
    print(f"\nLista modificada: {lista}")

main()
