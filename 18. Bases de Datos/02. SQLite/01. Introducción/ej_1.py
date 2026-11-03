'''
  En principio no se requiere tener más que Python instalado para poder trabajar con SQLite. Podemos desde nuestra 
  propia aplicación crear la base de datos y sus tablas.
'''

import sqlite3
from pathlib import Path

bbdd = Path(__file__).parent / 'bd1.db' # Creamos el fichero en la misma carpeta que el script.

conexion = sqlite3.connect(bbdd)
conexion.execute("CREATE TABLE articulos (codigo INTEGER PRIMARY KEY AUTOINCREMENT, descripcion VARCHAR(30), precio real)")

print("se creo la tabla articulos")

conexion.close()
