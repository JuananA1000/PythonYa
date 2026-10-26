'''
  Leer el contenido del archivo de texto 'datos.txt'.
'''

from pathlib import Path

ruta = Path(__file__).parent / 'datos.txt'
archivo = open(ruta, 'r', encoding='utf-8')

contenido = archivo.read()
print(contenido)

archivo.close()
