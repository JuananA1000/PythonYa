'''
  Confeccionar un módulo que implemente dos funciones, una que retorne el mayor de dos enteros y otra que retorne el 
  menor de dos enteros.

  En el módulo principal importar solo la función que retorne el mayor, luego cargar dos enteros y mostrar el mayor de 
  ellos

  Crear una carpeta llamada proyecto2 y dentro de la misma crear dos módulos llamados:

  mayormenor.py
  principal.py

  El módulo mayormenor.py contiene las dos funciones que identifican el mayor de dos enteros por un lado y el menor de 
  dos enteros.
'''

from mayormenor import el_mayor

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("\nEl mayor es:", el_mayor(num1, num2))
