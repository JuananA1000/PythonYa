import mysql.connector


class Articulos:
    def conexion(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd1",
            use_pure=True
        )
        return conexion

    # Ejercicio 1
    def alta(self, datos):
        cnx = self.conexion()
        cursor = cnx.cursor()
        sql = "INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)"
        cursor.execute(sql, datos)
        cnx.commit()
        cnx.close()

    def consulta(self, datos):
        cnx = self.conexion()
        cursor = cnx.cursor()
        sql = "SELECT * FROM articulos WHERE codigo = %s"
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        cnx.close()

        return resultado

    def listado(self):
        cnx = self.conexion()
        cursor = cnx.cursor()
        sql = "SELECT * FROM articulos"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cnx.close()

        return resultado

    # Ejercicio 2
    def baja(self, datos):
        cnx = self.conexion()
        cursor = cnx.cursor()
        sql = "DELETE FROM articulos WHERE codigo = %s"
        cursor.execute(sql, datos)
        cnx.commit()
        cnx.close()

    def actualizar(self, datos):
        cnx = self.conexion()
        cursor = cnx.cursor()
        sql = "UPDATE articulos SET descripcion = %s, precio = %s WHERE codigo = %s"
        cursor.execute(sql, datos)
        cnx.commit()
        cnx.close()
