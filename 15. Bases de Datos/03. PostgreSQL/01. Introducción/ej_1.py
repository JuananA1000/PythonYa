'''
  El primer programa que implementaremos nos conectaremos con el servidor de PostgreSQL e insertaremos un par de filas 
  en la tabla 'articulos' que creamos desde el programa 'pgAdmin'.
'''

import psycopg2

conexion = psycopg2.connect(
    database="bd1",
    user="postgres",
    password="123456",
    port="5432"
)

cursor = conexion.cursor()
sql = "INSERT INTO articulos(descripcion, precio) VALUES (%s,%s)"

datos = ("naranjas", 23.50)
cursor.execute(sql, datos)

datos = ("peras", 34)
cursor.execute(sql, datos)

datos = ("bananas", 25)
cursor.execute(sql, datos)

conexion.commit()
conexion.close()
