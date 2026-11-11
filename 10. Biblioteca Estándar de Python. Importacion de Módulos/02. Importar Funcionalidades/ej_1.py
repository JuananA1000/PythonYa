'''
  Confeccionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre la raíz cuadrada del 
  número y el valor elevado al cubo.

  Para resolver este problema utilizaremos dos funcionalidades que nos provee el módulo math de la biblioteca estándar 
  de Python.
'''

from math import sqrt
from math import pow

num = int(input('Ingresa un número: '))

print(f'√{num} = {sqrt(num):.2f}')
print(f'{num}³ = {pow(num, 3):.0f}')
