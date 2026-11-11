### 15.1.3 Otras Funcionalidades de mysql-connector

Hemos resuelto en los dos apartados anteriores algoritmos en Python que acceden a una base de datos de MySQL. Veremos otras funcionalidades que nos provee el paquete mysql-connector. Para utilizar cualquiera de estas funciones, también utilizaremos la función `cursor.execute()`. Algunas de estas otras funciones son:

- Inserción de múltiples filas en una tabla:
```python
cursor.execute("INSERT INTO nombre_tabla (campo1, campo2,...) VALUES (%s, %s,...)")
```

- Creación de una base de datos y tablas:
```python
cursor.execute("CREATE DATABASE nombre_bd") # Crear Base de Datos
cursor.execute("USE nombre_bd") # Utilizar Base de Datos
```

- Borrar una base de datos:
```python
cursor.execute("DROP DATABASE nombre_bd")
```

- Borrar una tabla en caso de que exista:
```python
cursor.execute("DROP TABLE IF EXISTS nombre_bd")
```
