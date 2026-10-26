'''
  Abrir un archivo de texto con el parámetro "r+", imprimir su contenido actual y agregar luego dos líneas al final.
'''

from pathlib import Path

ruta = Path(__file__).parent / 'datos.txt'

archivo = open(ruta, 'r+', encoding='utf-8')

contenido = archivo.read()
print(contenido)
archivo.write("Ej 6 -> Otra línea 1\n")
archivo.write("Ej 6 -> Otra línea 2\n")
archivo.close()
