'''
  Abrir el archivo de texto 'datos.txt' y luego agregar 2 líneas. Imprimir luego el archivo completo.
'''

from pathlib import Path

ruta = Path(__file__).parent / 'datos.txt'

archivo = open(ruta, 'a', encoding='utf-8')
archivo.write('Ej 5 -> Esta es otra línea más 1.\n')
archivo.write('Ej 5 -> Esta es otra línea más 2.\n')
archivo.close()

archivo = open(ruta, 'r', encoding='utf-8')
contenido = archivo.read()
print(contenido)
archivo.close()
