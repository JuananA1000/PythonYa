# Funcionalidades

Para desinstalar un paquete en nuestro equipo se hace indicando el comando 'uninstall':

```bash
pip uninstall nombre_del_paquete
```

Por ejemplo si queremos desinstalar el paquete **wxPython** que instalamos anteriormente, lo hacemos con la siguiente sintaxis:

```bash
pip uninstall wxPython
```

Si queremos conocer todos los archivos que tiene un paquete que hayamos instalado lo hacemos mediante la sintaxis:

```bash
pip show --files wxPython
```

Hay una sintaxis resumida para la misma actividad:

```bash
pip show -f wxPython
```

Para conocer todos los paquetes instalados en nuestro entorno de Python debemos utilizar el comando 'list':

```bash
pip list
```

Como podemos ver en el listado de paquetes además del paquete que instalamos en el concepto anterior hay otros que vienen por defecto cuando instalamos Python.

Los desarrolladores de paquetes para Python están constantemente actualizando sus funcionalidades. Para saber si alguno de nuestros paquetes está desactualizado podemos ejecutar el comando:

```bash
pip list --outdated
```

Si quisieramos instalar una versión concreta de un paquete debemos indicar en el comando 'install' la versión del mismo:

```bash
pip install wxPython==4.0.2
```

Para actualizar un paquete ya instalado debemos pasar el parámetro 'upgrade':

```bash
pip install --upgrade wxPython
```

Para profundizar y tener todas las actualizaciones del programa 'pip' debemos visitar la [guía de referencia oficial](https://pip.pypa.io/en/stable/user_guide/).