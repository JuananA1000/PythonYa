'''
  Almacenar una serie de strings en un archivo de texto. Tratar de llamar al método write() pasando un entero.
'''

from pathlib import Path

ruta = Path(__file__).parent / 'datos.txt'

try:
    archivo = open(ruta, 'w', encoding='utf-8')
    archivo.write('Primer string\n')
    archivo.write('Segundo string\n')
    archivo.write('Tercer string\n')
    archivo.write(1234)
except TypeError:
    print("No se puede escribir un entero en el archivo. Se esperaba un string.")
finally:
    archivo.close()
    print("Archivo cerrado correctamente.")
