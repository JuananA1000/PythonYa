## MySQL

Para crear y administrar bases de datos con python, necesitaremos instalar XAMPP

### ¿Qué es XAMPP?

XAMPP es un paquete gratuito que permite configurar un servidor web local en nuestro ordenador sin necesidad de contratar un servidor externo.

Incluye varias herramientas:

- **Apache:** servidor web que permite ejecutar aplicaciones localmente.
- **MariaDB:** sistema gestor de bases de datos compatible con MySQL.
- **phpMyAdmin:** interfaz gráfica para administrar bases de datos desde el navegador.
- **PHP:** lenguaje de programación utilizado para desarrollar aplicaciones web.

En nuestro caso, utilizaremos principalmente MariaDB y phpMyAdmin para gestionar bases de datos que posteriormente podremos utilizar desde Python.

### Descargar e instalar XAMPP

1. Accedemos a la página oficial: https://www.apachefriends.org/es/index.html
2. Descargamos la versión correspondiente a nuestro sistema operativo.
3. Ejecutamos el instalador descargado.
4. Seleccionamos los componentes que queremos instalar. Para trabajar con bases de datos necesitaremos Apache, MySQL (MariaDB) y phpMyAdmin.
5. Elegimos la carpeta de instalación (por ejemplo, `C:\xampp`).
6. Finalizamos la instalación.

### Utilizar el panel de control de XAMPP

Una vez instalado, abrimos XAMPP Control Panel.

Para trabajar con bases de datos:

1. Pulsamos **Start** en el apartado Apache.
2. Pulsamos **Start** en el apartado MySQL.
3. Si ambos servicios se inician correctamente, aparecerán resaltados en verde.
4. Abrimos nuestro navegador y accedemos a:

   http://localhost/phpmyadmin

Desde aquí podremos administrar nuestras bases de datos mediante una interfaz gráfica.

**Importante:** aunque el panel de XAMPP siga llamando MySQL al servicio, las versiones actuales de XAMPP incorporan MariaDB en lugar de MySQL. Ambos utilizan comandos y herramientas compatibles para las operaciones que vamos a estudiar.

### Crear una base de datos con phpMyAdmin

Para crear una nueva base de datos:

1. Accedemos a phpMyAdmin desde el navegador.
2. Seleccionamos la pestaña **Bases de datos**.
3. En el apartado de creación, introducimos el nombre de nuestra base de datos, por ejemplo `bd1`.
4. Seleccionamos una intercalación (por ejemplo, `utf8mb4_general_ci`).
5. Pulsamos **Crear**.

La base de datos aparecerá en el panel lateral izquierdo.

### Crear una tabla

Una vez creada la base de datos:

1. Seleccionamos `bd1` en el panel lateral.
2. Indicamos el nombre de la tabla, por ejemplo `articulos`.
3. Establecemos el número de columnas, por ejemplo `3`.
4. Pulsamos **Crear**.

Podemos definir los siguientes campos:

| Campo | Tipo | Propiedades |
|---|---|---|
| codigo | INT | PRIMARY KEY, AUTO_INCREMENT |
| descripcion | VARCHAR(50) | |
| precio | FLOAT | |

Finalmente, pulsamos **Guardar**.

### Insertar registros desde phpMyAdmin

Para introducir datos manualmente:

1. Seleccionamos la tabla `articulos`.
2. Accedemos a la pestaña **Insertar**.
3. Introducimos los valores de cada campo.
4. Pulsamos **Continuar** o **Guardar**.

También podemos insertar registros utilizando la pestaña **SQL**, escribiendo directamente una consulta:

```sql
INSERT INTO articulos (descripcion, precio)
VALUES
    ('Teclado', 25),
    ('Ratón', 15),
    ('Monitor', 150);
```

### Conectar Python con la base de datos creada

Una vez creada nuestra base de datos desde phpMyAdmin, podemos conectarnos a ella desde Python utilizando `mysql.connector`.

```python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd1",
    use_pure=True
)

cursor = conexion.cursor()

cursor.execute("SHOW TABLES")

for tabla in cursor:
    print(tabla)

cursor.close()
conexion.close()
```

Si todo funciona correctamente, obtendremos como resultado:

```text
('articulos',)
```

De esta manera podemos utilizar phpMyAdmin para crear y administrar nuestras bases de datos visualmente, mientras que Python nos permitirá realizar las mismas operaciones mediante código.

### Resumen

| Herramienta | Utilidad |
|---|---|
| XAMPP | Instala y gestiona el entorno de servidor local. |
| Apache | Servidor web necesario para acceder a phpMyAdmin. |
| MariaDB | Gestor de bases de datos. |
| phpMyAdmin | Interfaz gráfica para administrar bases de datos. |
| Python + mysql.connector | Permite gestionar las bases de datos mediante código. |

### Recursos oficiales

- [Página oficial de XAMPP](https://www.apachefriends.org/es/index.html)
- [Preguntas frecuentes e instalación de XAMPP](https://www.apachefriends.org/es/faq_windows.html)
- [Página oficial de phpMyAdmin](https://www.phpmyadmin.net/)

**Nota:** XAMPP está pensado para entornos locales de desarrollo y aprendizaje, no para desplegar servidores en producción.