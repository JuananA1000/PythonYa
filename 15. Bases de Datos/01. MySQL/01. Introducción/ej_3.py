'''
  Ahora implementaremos un programa que inserte un par de filas en la tabla 'articulos'.
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

sql = "INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)"

# Podemos insertar las filas de una en una...
datos = ("Blusa", 29.99)
cursor.execute(sql, datos)
datos = ("Abrigo", 59.99)
cursor.execute(sql, datos)

# ... o múltiples filas de una vez.
valores = [
    ("Camiseta", 19.99),
    ("Pantalón", 39.99)
]
cursor.executemany(sql, valores)

conexion.commit()
conexion.close()
