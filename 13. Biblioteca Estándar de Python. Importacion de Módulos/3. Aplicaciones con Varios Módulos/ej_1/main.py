'''
  Confeccionar una aplicación que permita cargar por teclado una lista de enteros, obtener y mostrar el mayor y calcular 
  su suma. Definir un módulo con las funciones de carga, identificar el mayor y sumar. En el módulo principal del 
  programa importar el otro módulo y llamar a sus funciones.

  Para ser un poco más ordenados crearemos una carpeta llamada proyecto1 y dentro de la misma crearemos los dos módulos 
  llamados:

  operacioneslista.py
  principal.py

  El módulo operacioneslista.py contiene todas las funciones que nos permiten cargar una lista, imprimir el mayor de 
  una lista y sumar todos los elementos y mostrar dicho valor.
'''

from operacioneslista import cargar, imprimir_mayor, imprimir_suma

lista = cargar()
imprimir_mayor(lista)
imprimir_suma(lista)
