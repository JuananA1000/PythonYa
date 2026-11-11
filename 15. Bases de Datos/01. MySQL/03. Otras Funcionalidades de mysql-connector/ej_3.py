'''
  En conceptos anteriores vimos como crear una base de datos de MySQL utilizando la aplicación PHPMyAdmin, en algunas 
  situaciones podemos necesitar crear una base de datos desde el mismo programa de Python. La misma metodología será si 
  queremos crear tablas.
'''

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    use_pure=True
)
cursor = conexion.cursor()

sql = "CREATE DATABASE bd2"
cursor.execute(sql)

sql = "USE bd2"
cursor.execute(sql)

sql = "CREATE TABLE usuarios (nombre VARCHAR(30) PRIMARY KEY, clave VARCHAR(30))"
cursor.execute(sql)

conexion.commit()
conexion.close()
