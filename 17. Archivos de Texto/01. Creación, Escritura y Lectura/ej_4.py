'''
  Leer el contenido del archivo de texto 'datos.txt' y almacenar sus líneas en una lista. Imprimir la cantidad de líneas \
  que tiene el archivo y su contenido.
'''

from pathlib import Path

ruta = Path(__file__).parent / 'datos.txt'
archivo = open(ruta, 'r', encoding='utf-8')
lineas = archivo.readlines()
archivo.close()

print(f"El archivo tiene {len(lineas)} líneas.")
for linea in lineas:
    print(linea, end='')
