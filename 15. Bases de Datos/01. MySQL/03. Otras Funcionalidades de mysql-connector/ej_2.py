'''
  La clase cursor a parte del método 'execute' cuenta con otro método llamado 'executemany' que tiene el objetivo de 
  insertar múltiples filas de una tabla.
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
sql = "INSERT INTO articulos(descripcion, precio) VALUES (%s,%s)"
datos = [("naranjas", 23.50),
         ("bananas", 34),
         ("peras", 21),
         ("sandía", 19.60)]
cursor.executemany(sql, datos)
conexion.commit()
conexion.close()
