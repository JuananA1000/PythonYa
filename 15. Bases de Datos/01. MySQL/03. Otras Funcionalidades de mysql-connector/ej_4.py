'''
  Cuando queremos crear una base de datos que ya existe se genera un error, podemos primero borrarla y luego ya 
  crearla sin problemas.
'''

import mysql.connector

conexion = mysql.connector.connect(host="localhost",
                                   user="root",
                                   use_pure=True,
                                   passwd="")
cursor = conexion.cursor()

sql = "DROP DATABASE IF EXISTS bd2"
cursor.execute(sql)

sql = "CREATE DATABASE bd2"
cursor.execute(sql)

sql = "USE bd2"
cursor.execute(sql)

sql = "CREATE TABLE usuarios (nombre VARCHAR(30) PRIMARY KEY, clave  VARCHAR(30))"
cursor.execute(sql)

conexion.commit()
conexion.close()
