'''
  REALIZAR SIN EXCEPCIONES
  Realizar la carga de dos números enteros por  teclado e imprimir su suma, luego preguntar si quiere seguir sumando 
  valores.
  Codificar dos programas uno que capture la excepción de ingreso de datos no numéricos y el otro que no tenga en cuenta 
  el tipo de entrada de datos.
'''

while True:
    v1 = int(input("Valor 1: "))
    v2 = int(input("Valor 2: "))

    suma = v1 + v2

    print(f"La suma es: {suma}")

    continuar = input("¿Desea continuar? (s/n): ")

    if continuar == "n":
        break
