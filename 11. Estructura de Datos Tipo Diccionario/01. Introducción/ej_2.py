'''
  Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor el 
  precio del mismo.
  
  Desarrollar además las funciones de:
  a) Imprimir en forma completa el diccionario
  
  b) Imprimir solo los artículos con precio superior a 100.
'''

def imprimir_superiores(productos):
    lista = []
    for i in productos:
        if productos[i] > 100:
            lista.append(i)
    return lista

def main():
    productos = {"Galletas": 100, "Chocolates": 200, "Chicles": 300}

    print("Diccionario completo")
    for producto in productos:
        print(f'{producto}: {productos[producto]}')

    print("\nArtículos superiores a 100")
    print(imprimir_superiores(productos))

main()
