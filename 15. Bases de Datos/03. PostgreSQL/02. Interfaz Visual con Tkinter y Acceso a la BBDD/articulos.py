import psycopg2


class Articulos:

    def abrir(self):
        conexion = psycopg2.connect(database="bd1", user="postgres", password="123456")
        return conexion

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "insert into articulos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        return cursor.fetchall()

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        return cursor.fetchall()

    # Ejercicio 2

    def borrar(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def modificar(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
