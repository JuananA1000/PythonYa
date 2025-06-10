'''
  Confeccionar un programa que simule tirar dos dados y luego muestre los valores que salieron. Imprimir un mensaje que 
  ganó si la suma de los mismos es igual a 7.
  
  Para resolver este problema requerimos un algoritmo para que se genere un valor aleatorio entre 1 y 6. Como la 
  generación de valores aleatorios es un tema muy frecuente la biblioteca estándar de Python incluye un módulo que nos 
  resuelve la generación de valores aleatorios.
'''

import random

valor1 = random.randint(1, 6)
valor2 = random.randint(1, 6)

print("Valor del dado 1:", valor1)
print("Valor del dado 2:", valor2)

if valor1 + valor2 == 7:
    print(f"Resultado: {valor1} + {valor2} = {valor1 + valor2}. Ganó")
else:
    print(f"Resultado: {valor1} + {valor2} = {valor1 + valor2}. Perdió")
