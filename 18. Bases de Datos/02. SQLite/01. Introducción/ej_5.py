'''
  Implementaremos un programa que solicite el ingreso de un precio y luego nos muestre la descripción de todos los 
  artículos con un precio inferior al ingresado.
'''

import sqlite3
from pathlib import Path

bbdd = Path(__file__).parent / 'bd1.db'

conexion = sqlite3.connect(bbdd)

precio = float(input("Ingrese un precio:"))

cursor = conexion.execute("SELECT descripcion, precio FROM articulos WHERE precio < ?", (precio, ))
filas = cursor.fetchall()

if len(filas) > 0:
    for fila in filas:
        print(fila)
else:
    print(f"No existen artículos con un precio menor a {precio}.")
conexion.close()
