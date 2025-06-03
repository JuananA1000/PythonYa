'''
  Confeccionar un programa que permita cargar un código de producto como clave en un diccionario. Guardar para dicha
  clave el nombre del producto, su precio y cantidad en stock.

  Implementar las siguientes actividades:
  a) Carga de datos en el diccionario.

  b) Listado completo de productos.

  c) Consulta de un producto por su clave, mostrar el nombre, precio y stock.

  d) Listado de todos los productos que tengan un stock con valor cero.
'''


def imprimir(productos):
    print("\nListado completo de productos:")
    for codigo in productos:
        print(
            f"COD: {codigo} DESC: {productos[codigo][0]} PRECIO: {productos[codigo][1]}€ STOCK: {productos[codigo][2]}")


def consulta(productos):
    codigo = int(input("Ingrese el codigo de articulo a consultar: "))
    if codigo in productos:
        print(productos[codigo][0], productos[codigo][1], productos[codigo][2])


def listado_stock_cero(productos):
    print("Listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2] == 0:
            print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])


def main():
    productos = {}
    continua = "s"
    i = 0

    while continua == "s":
        print(f"\nPRODUCTO [{i+1}]:")
        codigo = int(input("Código:"))
        descripcion = input("Descripción:")
        precio = float(input("Precio:"))
        stock = int(input("Stock actual:"))
        productos[codigo] = (descripcion, precio, stock)
        continua = input("Desea cargar otro producto[s/n]?: ")

    imprimir(productos)
    print("\n")
    consulta(productos)
    print("\n")
    listado_stock_cero(productos)
    print("\n")


main()
