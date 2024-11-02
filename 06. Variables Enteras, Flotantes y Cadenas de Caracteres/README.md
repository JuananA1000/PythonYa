
# Variables enteras, flotantes y cadenas de caracteres

Hasta ahora, hemos visto como definir variables. Las hemos cargado **por asignación**, con el operador '='...

```
cantidad = 20 # variable entera
altura = 1.92 # variable flotante
```

y **por teclado**.

```
cantidad = int(input("Cantidad de personas: "))
altura = float(input("Altura de la persona en metros ej: 1.70:"))
```

El intérprete de Python diferencia entre **variables flotantes** y **enteras** por el caracter punto, y para cargarlas por teclado mediante **input()** usaremos la función **int()** o **float()** para convertir el dato introducido.

A estos dos tipos de datos se suman las **cadenas de caracteres**, compuestas por uno o más caracteres, que podremos inicializarlas por asignación:

```
dia1 = "lunes" # Con comillas dobles
dia2 = 'martes' # Con comillas simples
```
o por teclado.

```
nombre = input("Ingrese su nombre: ")
```