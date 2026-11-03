### Introducción

#### Paquetes necesarios

Para conectar Python con una base de datos MySQL necesitamos instalar el conector oficial:

```bash
python -m pip install mysql-connector-python
```

Si utilizamos una instalación concreta de Python en Windows:

```powershell
C:\Python310\python.exe -m pip install mysql-connector-python
```

**Importante:**
- Instalar únicamente `mysql-connector-python`.
- No instalar el paquete antiguo `mysql-connector`.
- No es necesario instalar `mysqlclient` ni otros conectores para este ejemplo.

Documentación oficial: https://dev.mysql.com/doc/connector-python/en/

#### Instalar XAMPP

XAMPP incluye Apache, MariaDB, PHP y phpMyAdmin.

Descarga oficial: https://www.apachefriends.org/es/download

Una vez instalado:

1. Abre el **XAMPP Control Panel**.
2. Pulsa **Start** en el módulo MySQL para iniciar el servidor de bases de datos.
3. Si necesitas administrar bases de datos desde el navegador, inicia también Apache.

#### Acceder a phpMyAdmin

Abre el navegador y visita:

http://localhost/phpmyadmin

Desde phpMyAdmin puedes crear bases de datos, crear tablas, insertar registros y ejecutar consultas SQL.

#### Ejemplo de conexión desde Python

Este programa se conecta al servidor local, muestra las bases de datos disponibles y cierra la conexión.

```python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    use_pure="True"
)

cursor = conexion.cursor()
cursor.execute("SHOW DATABASES")

for base in cursor:
    print(base[0])

cursor.close()
conexion.close()
```

**Nota:** el ejemplo supone que el usuario `root` no tiene contraseña. Si has configurado una, debes introducirla en `password`. Si utilizas el servidor de XAMPP, recuerda que normalmente se trata de MariaDB.
**Nota 2:** El parámetro `use_pure=True` indica al conector `mysql-connector` que utilice su implementación escrita íntegramente en Python, en lugar de utilizar la implementación basada en C.

#### Errores frecuentes

- `ModuleNotFoundError`: instalar el conector con el mismo intérprete de Python que ejecuta el programa.
- `Can't connect to MySQL server`: comprobar que el servicio MySQL/MariaDB está iniciado y que el puerto es correcto.
- `Access denied`: revisar el usuario y la contraseña.
- `Segmentation fault`: comprobar la instalación del conector y aislar el error antes de reinstalar paquetes.

#### 6. Resumen

- **Python:** ejecuta el programa.
- **mysql-connector-python:** permite que Python se comunique con el servidor.
- **XAMPP / MariaDB:** proporciona el servidor de bases de datos.
- **phpMyAdmin:** permite administrar las bases de datos desde el navegador.