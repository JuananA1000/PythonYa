'''
  Implementaremos un programa que solicite ejecutar un 'select' en la tabla 'articulos' y nos retorne todas sus filas.
'''

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd1",
    use_pure=True
)

cursor = conexion.cursor()

sql = "SELECT * FROM articulos"

cursor.execute(sql)

for fila in cursor:
    print(fila)
    
conexion.close()
