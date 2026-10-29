'''
  El primer programa que implementaremos nos conectaremos con el servidor de MySQL y mostraremos todas las bases de datos 
  existentes
'''

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    use_pure=True
)

cursor = conexion.cursor()
cursor.execute("SHOW DATABASES")

for bbdd in cursor:
    print(bbdd)

cursor.close()
conexion.close()
