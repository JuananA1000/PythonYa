'''
  Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar otro valor debiendo 
  el operador ingresar la cadena 'si' o 'no' por teclado.
  Mostrar la suma de los valores ingresados.
'''

opcion = 's'
suma = 0
while opcion == 's':
    valor = int(input("Ingrese un valor: "))
    suma = suma + valor
    opcion = input("Desea cargar otro numero (s/n): ")

print("\nLa suma de valores ingresados es: ", suma)
