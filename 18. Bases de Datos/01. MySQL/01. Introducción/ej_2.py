'''
  Ahora implementaremos un programa que recupere todas las tablas contenidos en una base de datos. Trabajaremos con la 
  base de datos que creamos desde el PHPMyAdmin llamada 'bd1'.
'''

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd1", # Seleccionamos aquí la base de datos a mostrar
    use_pure=True
)

cursor = conexion.cursor()
cursor.execute("SHOW TABLES") # El comando 'SHOW TABLES' nos devuelve todas las tablas de la bbdd seleccionada

for tabla in cursor:
    print(tabla)

cursor.close()
conexion.close()
