'''
  Realizar la carga de valores enteros y sumarlos, cada vez que se ingresa un valor preguntar al operador si desea 
  ingresar otro valor.
'''

opciones_salir = frozenset(["no", "NO"])
suma = 0

while True:
    valor = int(input("Ingrese un valor:"))
    suma = suma + valor
    op = input("Desea ingresar otro valor: [si/no]")

    if op in opciones_salir:
        break

print(f"La suma de los valores es {suma}")
