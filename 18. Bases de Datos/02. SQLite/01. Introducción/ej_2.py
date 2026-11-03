'''
  Ahora implementaremos un programa que inserte un par de filas en la tabla 'articulos' de la base de datos 'bd1' que 
  acabamos de crear con el programa anterior.
'''
import sqlite3
from pathlib import Path

bbdd = Path(__file__).parent / 'bd1.db'

conexion = sqlite3.connect(bbdd)

conexion.execute("INSERT INTO articulos (descripcion, precio) VALUES ('naranjas', 23.50)")
conexion.execute("INSERT INTO articulos (descripcion, precio) VALUES ('peras', 34)")
conexion.execute("INSERT INTO articulos (descripcion, precio) VALUES ('bananas', 25)")

conexion.commit()
conexion.close()
