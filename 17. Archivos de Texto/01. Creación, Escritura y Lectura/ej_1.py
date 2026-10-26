'''
  Crear un archivo de texto llamado 'datos.txt', almacenar tres líneas de texto. Abrir luego el archivo creado con un 
  editor de texto.
'''

from pathlib import Path

ruta = Path(__file__).parent / 'datos.txt'  # Usamos Path para crear 'datos.txt' en el mismo directorio que este script.

archivo = open(ruta, 'w', encoding='utf-8')
archivo.write('Esta es la primera línea.\n')
archivo.write('Esta es la segunda línea.\n')
archivo.write('Esta es la tercera línea.\n')
archivo.close()
