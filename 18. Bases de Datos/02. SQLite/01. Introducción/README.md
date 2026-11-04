### 18.2.1 Introducción

A diferencia de MySQL, SQLite **almacena toda la información en un único archivo**, normalmente con extensión `.db` o `.sqlite`.

#### Características principales

- Ligero: no necesita un servidor como MySQL.
- Integrado en Python: dispone del módulo sqlite3, que viene incluido en Python.
- Portátil: toda la base de datos se almacena en un archivo.
- SQL: permite realizar consultas, inserciones, modificaciones y eliminaciones mediante sentencias SQL.
- Ideal para: aplicaciones pequeñas, proyectos personales, prototipos y aplicaciones de escritorio.

#### Conexión con SQLite desde Python

Para trabajar con SQLite utilizaremos el módulo sqlite3, que no necesita instalarse mediante pip.

Ejemplo de conexión

```python
import sqlite3

conexion = sqlite3.connect("basedatos.db")
cursor = conexion.cursor()
cursor.execute("...") # Incluir la consulta
conexion.commit() # Guardamos los cambios

# Mostramos los resultados
registros = cursor.fetchall()

for registro in registros:
    print(registro)

conexion.close()
```
