'''
  Realizar la carga de dos números por  teclado e imprimir la división del primero respecto al segundo, capturar la 
  excepción ZeroDivisionError.
'''

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")