'''
  Implementaremos un programa que solicite ejecutar un 'select' en la tabla 'articulos' de la base de datos 'bd1' y nos 
  retorne todas sus filas.
'''

import psycopg2

conexion = psycopg2.connect(
  database="bd1", 
  user="postgres", 
  password="123456"
)

cursor = conexion.cursor()
cursor.execute("SELECT codigo, descripcion, precio FROM articulos")

for fila in cursor:
    print(fila)

conexion.close()
