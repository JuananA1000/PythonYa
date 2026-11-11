'''
  Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el 
  precio.
  Desarrollar las funciones:
  
  a) Cargar por teclado.
  
  b) Listar los productos y precios.
  
  c) Imprimir los productos con precios comprendidos entre 10 y 15. 
'''

def listar_productos(li):
    for nombre, precio in li:
        print(f'{nombre}: {precio}')

def imprimir_productos_entre_10_y_15(li):
    for nombre, precio in li:
        if precio >= 10 and precio <= 15:
            print(f'{nombre}: {precio}')

def main():
    productos = []
    for i in range(5):
        print(f'\n-- PRODUCTO {i+1} --')
        nombre = input(f'Nombre: ')
        precio = float(input(f'Precio: '))
        productos.append((nombre, precio))

    print('\nLista de productos:')
    listar_productos(productos)

    print('\nProductos entre 10€ y 15€:')
    imprimir_productos_entre_10_y_15(productos)

main()
