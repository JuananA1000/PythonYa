'''
  Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba la lista y nos 
  retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa. 
'''

def producto(lista):
    prod = 1

    i = 0
    while i < len(lista):
        prod = prod * lista[i]
        i += 1
    return prod

def main():
    lista = [10, 7, 3, 7, 2]

    producto_lista = producto(lista)
    print(f'El producto de todos sus elementos es: {producto_lista}.')

main()