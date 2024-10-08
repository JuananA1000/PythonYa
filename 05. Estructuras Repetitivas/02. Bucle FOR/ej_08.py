'''
  Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de
  un triángulo. El programa deberá informar:

  a) De cada triángulo la medida de su base, su altura y su superficie.
  
  b) La cantidad de triángulos cuya superficie es mayor a 12.
'''

n = int(input("Ingrese la cantidad de triángulos: "))
contador_superficie_mayor_12 = 0

for i in range(n):
    print(f"\nTriángulo {i+1}:")
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    superficie = (base * altura)/2

    print(f"Base: {base}, Altura: {altura}, Superficie: {superficie:.2f}")

    if superficie > 12:
        contador_superficie_mayor_12 += 1

print(
    f"\nCantidad de triángulos con superficie mayor a 12: {contador_superficie_mayor_12}")
