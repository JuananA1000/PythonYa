### 15.3.1 Introducción
Para crear una primera conexión para Python y Postgre, crearemos un archivo `nombre_archivo.py`:

```python
import psycopg

conexion = psycopg.connect(
    database="nombre_bbdd",
    user="postgres",
    password="tu_contraseña", # La que hayas asignado al crear una primera conexión a tu Base de Datos
    host="localhost",
    port="5432" # El puerto por defecto en Postgre
)

print("Conexión establecida correctamente")

conexion.close()
```

Si el programa se ejecuta sin errores, habremos conectado Python con PostgreSQL.
 
> [!IMPORTANT]
> En proyectos reales, evita escribir las contraseñas directamente en el código. Utiliza variables de entorno.
