import sqlite3
from pathlib import Path


class Articulos:

    # Ejercicio 1
    def abrir(self):
        bbdd = Path(__file__).parent.parent / 'bd1.db'
        conexion = sqlite3.connect(bbdd)

        return conexion

    def alta(self, datos):
        cnx = self.abrir()
        cursor = cnx.cursor()
        sql = "INSERT INTO articulos(descripcion, precio) VALUES (?,?)"
        cursor.execute(sql, datos)
        cnx.commit()
        cnx.close()

    def consulta(self, datos):
        try:
            cnx = self.abrir()
            cursor = cnx.cursor()
            sql = "SELECT descripcion, precio FROM articulos WHERE codigo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cnx.close()

    def recuperar_todos(self):
        try:
            cnx = self.abrir()
            cursor = cnx.cursor()
            sql = "SELECT codigo, descripcion, precio FROM articulos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cnx.close()

    # Ejercicio 2
    def baja(self, datos):
        try:
            cnx = self.abrir()
            cursor = cnx.cursor()
            sql = "DELETE FROM articulos WHERE codigo=?"
            cursor.execute(sql, datos)
            cnx.commit()
        finally:
            cnx.close()
        cnx.close()

    def actualizar(self, datos):
        try:
            cnx = self.abrir()
            cursor = cnx.cursor()
            sql = "UPDATE articulos SET descripcion = ?, precio = ? WHERE codigo = ?"
            cursor.execute(sql, datos)
            cnx.commit()
        finally:
            cnx.close()
    
