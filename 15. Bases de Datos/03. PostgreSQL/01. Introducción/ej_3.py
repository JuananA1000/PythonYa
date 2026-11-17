'''
  Las otras dos actividades fundamentales que podemos hacer con una tabla es borrar filas y modificar datos.
  Desarrollaremos un pequeño programa que borre el artículo cuyo código sea el 1 y modifique el precio del artículo cuyo 
  código sea 3.
'''

import psycopg2

conexion = psycopg2.connect(
    database="bd1",
    user="postgres",
    password="123456"
)

cursor = conexion.cursor()
cursor.execute("DELETE from articulos where codigo=1")
cursor.execute("UPDATE articulos SET precio=50 WHERE codigo=3")
conexion.commit()
cursor.execute("SELECT codigo, descripcion, precio FROM articulos")

for fila in cursor:
    print(fila)
    
conexion.close()
