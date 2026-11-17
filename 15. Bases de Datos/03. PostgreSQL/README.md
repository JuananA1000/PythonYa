## 15.3 PostgreSQL

### Instalar PostgreSQL

PostgreSQL es un sistema gestor de bases de datos relacional que permite almacenar y gestionar información.

1. Accede a la página oficial haciendo click [aquí](https://www.postgresql.org/download/windows/ 'aquí')
2. Descarga el instalador para tu Sistema Operativo.
3. Ejecuta el instalador y sigue los pasos.
4. Durante la instalación, establece una contraseña para el usuario `postgres`.
5. Mantén el puerto predeterminado `5432`.
6. Instala también **pgAdmin 4**, que permite administrar las bases de datos mediante una interfaz gráfica.

### Instalar Psycopg en Python

Psycopg es una librería que permite conectar Python con PostgreSQL y ejecutar consultas SQL.

Desde la terminal de nuestro proyecto, ejecutamos:

```bash
pip install psycopg2"
```

Para comprobar que se ha instalado correctamente:

```bash
pip show psycopg2
```
