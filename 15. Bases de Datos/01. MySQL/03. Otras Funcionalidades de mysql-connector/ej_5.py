'''
  No se puede crear una tabla con el mismo nombre de una existente, en esos casos debemos borrar la actual y crear una 
  nueva.
'''

import mysql.connector

conexion = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    use_pure=True,
                                    database="bd2")
cursor = conexion.cursor()

sql = "DROP TABLE IF EXISTS usuarios"
cursor.execute(sql)

sql = "CREATE TABLE usuarios (nombre VARCHAR(30) PRIMARY KEY, clave VARCHAR(30))"
cursor.execute(sql)

conexion.commit()
conexion.close()
