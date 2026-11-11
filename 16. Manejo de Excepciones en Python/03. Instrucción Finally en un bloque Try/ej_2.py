'''
  Conectarse a una base de datos de MySQL y ejecutar un comando SQL incorrecto.
'''

import mysql.connector

try:
    conexion1 = mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="",
        database="bd2",
        use_pure=True
    )
    cursor1 = conexion1.cursor()
    cursor1.execute("INSERT INTO usuarios (nombre, clave) VALUES ('juan', 'clave123')")
    conexion1.commit()
except mysql.connector.errors.ProgrammingError:
    print("Error en el comando SQL")
finally:
    conexion1.close()
    print("Se cerró la conexión a la base de datos")
