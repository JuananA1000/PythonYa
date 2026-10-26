'''
  Leer el contenido del archivo de texto 'datos.txt' línea a línea.
'''

from pathlib import Path

ruta = Path(__file__).parent / 'datos.txt'
archivo = open(ruta, 'r', encoding='utf-8')
linea = archivo.readline()

while linea != '':
    print(linea, end=' ')
    linea = archivo.readline()

archivo.close()
