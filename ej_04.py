'''
  Introduce el precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en
  el precio del producto)
'''

precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos a llevar: "))

importe = precio * cantidad

print("El importe a pagar es: ", importe, '€')
