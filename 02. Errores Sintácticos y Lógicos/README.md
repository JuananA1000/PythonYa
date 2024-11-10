# Errores sintácticos y lógicos

En Python, los **errores al escribir o ejecutar código** se dividen en dos tipos principales: **errores sintácticos** y **errores lógicos**.
Comprender y diferenciar los distintos errores es fundamental para un código funcional y fácil de depurar.

## Errores sintácticos

Estos errores son detectados por el intérprete de Python, **antes de ejecutar el programa**. Algunos errores tipográficos, llamados **errores sintácticos**, son:

- Indicar el nombre incorrecto de la función
- Nombres de variables incorrectas
- Falta de paréntesis
- Palabras claves mal escritas

Sin corregir todos estos errores, un programa no se ejecuta.

### Ejemplo de error sitáctico

_Hallar la superficie de un cuadrado conociendo el valor de un lado._

```
lado = int(input("Lado del cuadrado: "))
superficie = lado * lado

print("La superficie del cuadrado es: ", Superficie)
```

> [!CAUTION]  
> La variable "Superficie" **no existe**, debemos respetar como la iniciamos anteriormente.

Este sería un programa correctamente codificado:

```
lado = int(input("Lado del cuadrado: "))
superficie = lado * lado

print("La superficie del cuadrado es: ", superficie)
```

## Errores lógicos

Los **errores lógicos**, en programas grandes, de miles de líneas, son más difíciles de localizar. Por ejemplo un programa que permite hacer la facturación pero la salida de datos por impresora es incorrecta.

### Ejemplo de error lógico:

_Hallar la superficie de un cuadrado conociendo el valor de un lado._

```
lado = int(input("Lado del cuadrado: "))
superficie = lado * lado * lado

print("La superficie del cuadrado es: ", superficie)
```

> [!WARNING]  
> Si ejecutamos el programa **no presenta ningún error sintáctico**, pero al ingresar el valor del lado del cuadrado, obtenemos un valor incorrecto. Esto se debe a que definimos incorrectamente la fórmula para calcular la superficie del cuadrado.
