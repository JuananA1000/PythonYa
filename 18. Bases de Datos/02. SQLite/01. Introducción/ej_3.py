'''
  Implementaremos un programa que solicite ejecutar un 'select' en la tabla 'articulos' y nos retorne todas sus filas.
'''

import sqlite3
from pathlib import Path

bbdd = Path(__file__).parent / 'bd1.db'

conexion = sqlite3.connect(bbdd)
cursor = conexion.execute("SELECT codigo, descripcion, precio FROM articulos")

for fila in cursor:
    print(fila)
    
conexion.close()