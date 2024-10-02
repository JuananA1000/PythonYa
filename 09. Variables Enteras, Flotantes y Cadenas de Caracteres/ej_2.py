'''
  Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabéticamente* o si son iguales.

  *Mayor posición en el alfabeto: c = 3 | l = 12 --> l > c, porque 12 > 3
'''

nom1 = input("Ingrese el primer nombre: ")
nom2 = input("Ingrese el segundo nombre: ")

if nom1 == nom2:
    print("Los nombres son iguales")
else:
    if nom1 > nom2:
        print(f"{nom1} es mayor alfabéticamente")
    else:
        print(f"{nom2} es mayor alfabéticamente")
