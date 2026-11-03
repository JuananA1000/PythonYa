'''
  Implementaremos un programa que solicite el ingreso del código de un producto y luego nos muestre su descripción y 
  precio.
'''

import sqlite3
from pathlib import Path

bbdd = Path(__file__).parent / 'bd1.db'

conexion = sqlite3.connect(bbdd)

codigo = int(input("Ingrese el código de un artículo: "))

cursor = conexion.execute("SELECT descripcion, precio FROM articulos WHERE codigo=?", (codigo, ))
fila = cursor.fetchone()

if fila != None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()
