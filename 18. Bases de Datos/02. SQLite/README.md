## 18.2. SQLite

La segunda base de datos que veremos su acceso desde Python es SQLite.

SQLite es un gestor de bases de datos diferente a MySQL, SQLServer, Oracle etc.
Este gestor de base de datos **forma parte de la misma aplicación con la que colabora**, porque no cumple los conceptos de cliente y servidor.

Para entender sus usos podemos dar algunos ejemplos donde se utiliza el gestor SQLite es un gestor de bases de datos utilizado por navegadores como **Firefox** u **Opera**, aplicaciones como **Skype** de Microsoft utiliza SQLite, o sistemas operativos como **Android** y **iOS** para almacenar y recuperar datos.

SQLite es Open Source y está instalado por defecto con Python, no tenemos que instalar ningún módulo con pip.

Si nuestra aplicación necesita almacenar gran cantidad de información local con cierta estructura el empleo de SQLite es nuestra principal opción.
