'''
  Cuando insertamos una fila en una tabla que contiene un campo que se auto incrementa podemos recuperar dicho valor en 
  el mismo momento que efectuamos la inserción.
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
sql = "INSERT INTO articulos(descripcion, precio) VALUES (%s,%s)"
datos = ("naranjas", 23.50)
cursor.execute(sql, datos)
conexion.commit()
print("Valor del último código de artículo generado:", cursor.lastrowid)
conexion.close()
