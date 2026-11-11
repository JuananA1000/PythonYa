'''
  Realizar el programa anterior con excepciones
'''

while True:
    try:
        v1 = int(input("Valor 1: "))
        v2 = int(input("Valor 2: "))

        suma = v1 + v2

        print(f"La suma es: {suma}")

    except ValueError:
        print("Error: Por favor, ingrese solo números enteros.")

    continuar = input("¿Desea continuar? (s/n): ")
    if continuar == "n":
        break
