## 16.2 Excepciones Estándar de Python

Las **excepciones** son errores que se producen durante la ejecución de un programa. Python incluye excepciones para identificar distintos problemas y permitir que los controlemos mediante `try` y `except`.

### Cómo controlar excepciones

```python
try:
    numero = int(input("Introduce un número: "))
    print(10 / numero)
except ValueError:
    print("Debes introducir un número")
except ZeroDivisionError:
    print("No puedes dividir entre cero")
```

- `try`: contiene el código que puede fallar.
- `except`: indica cómo responder a una excepción.
- `as error`: permite guardar el mensaje del error en una variable.

```python
try:
    numero = int("hola")
except ValueError as error:
    print(error)
```

### Excepciones generales

| Excepción | Definición | Ejemplo |
|---|---|---|
| `BaseException` | Clase base de todas las excepciones. | `raise BaseException("Error")` |
| `Exception` | Clase base habitual para errores que se pueden controlar. | `raise Exception("Error")` |
| `BaseExceptionGroup` | Agrupa varias excepciones, incluidas las que no heredan de `Exception`. | `raise BaseExceptionGroup("Errores", [KeyboardInterrupt()])` |
| `ExceptionGroup` | Agrupa varias excepciones derivadas de `Exception`. | `raise ExceptionGroup("Errores", [ValueError(), TypeError()])` |

Normalmente, las excepciones propias deben heredar de `Exception`, no directamente de `BaseException`.

### Errores de operaciones y valores

| Excepción | Definición | Ejemplo |
|---|---|---|
| `ArithmeticError` | Clase base de errores aritméticos. | `raise ArithmeticError("Error aritmético")` |
| `FloatingPointError` | Error en una operación de coma flotante; poco habitual en Python estándar. | `raise FloatingPointError()` |
| `OverflowError` | Una operación numérica supera el rango permitido. | `import math; math.exp(10000)` |
| `ZeroDivisionError` | División o módulo entre cero. | `10 / 0` |
| `AssertionError` | Falla una comprobación `assert`. | `assert 2 > 5` |
| `TypeError` | Se utiliza un tipo de dato incompatible. | `"2" + 2` |
| `ValueError` | El tipo es correcto, pero el valor no es válido. | `int("hola")` |

### Variables, atributos y referencias

| Excepción | Definición | Ejemplo |
|---|---|---|
| `NameError` | Se utiliza un nombre que no existe. | `print(variable_inexistente)` |
| `UnboundLocalError` | Se accede a una variable local antes de asignarle un valor. | `def f():`<br/>`    print(x)`<br/>`    x = 1` |
| `AttributeError` | Un objeto no tiene el atributo solicitado. | `(5).append(1)` |
| `ReferenceError` | Se intenta acceder a un objeto mediante una referencia débil que ya no es válida. | `raise ReferenceError()` |

### Listas, diccionarios y secuencias

| Excepción | Definición | Ejemplo |
|---|---|---|
| `LookupError` | Clase base de errores al buscar elementos. | `raise LookupError()` |
| `IndexError` | Índice fuera de los límites de una secuencia. | `[1, 2][5]` |
| `KeyError` | Clave inexistente en un diccionario. | `{"nombre": "Ana"}["edad"]` |

### Archivos, sistema y permisos

`OSError` es la clase base de muchos errores relacionados con el sistema operativo, archivos, directorios y conexiones.

| Excepción | Definición | Ejemplo |
|---|---|---|
| `OSError` | Error del sistema operativo. | `open("ruta_inexistente.txt")` |
| `BlockingIOError` | Una operación de entrada/salida no puede completarse porque bloquearía. | `raise BlockingIOError()` |
| `ChildProcessError` | Error relacionado con la gestión de un proceso hijo. | `raise ChildProcessError()` |
| `FileExistsError` | Se intenta crear un archivo o directorio que ya existe. | `raise FileExistsError()` |
| `FileNotFoundError` | No se encuentra el archivo o directorio. | `open("no_existe.txt")` |
| `IsADirectoryError` | Se intenta tratar un directorio como si fuera un archivo. | `open(".")` |
| `NotADirectoryError` | Una parte de la ruta debería ser un directorio, pero no lo es. | `raise NotADirectoryError()` |
| `PermissionError` | No hay permisos suficientes para realizar una operación. | `raise PermissionError()` |
| `InterruptedError` | Una operación del sistema se interrumpe por una señal. | `raise InterruptedError()` |
| `ProcessLookupError` | No se encuentra el proceso solicitado. | `raise ProcessLookupError()` |
| `TimeoutError` | Una operación supera el tiempo de espera permitido. | `raise TimeoutError()` |

#### Errores de conexión

| Excepción | Definición | Ejemplo |
|---|---|---|
| `ConnectionError` | Clase base de errores de conexión. | `raise ConnectionError()` |
| `BrokenPipeError` | Se escribe en una conexión cuyo extremo de lectura se ha cerrado. | `raise BrokenPipeError()` |
| `ConnectionAbortedError` | Una conexión se interrumpe durante su establecimiento o uso. | `raise ConnectionAbortedError()` |
| `ConnectionRefusedError` | El destino rechaza una conexión. | `raise ConnectionRefusedError()` |
| `ConnectionResetError` | El otro extremo reinicia la conexión. | `raise ConnectionResetError()` |

#### Otros errores del sistema

| Excepción | Definición | Ejemplo |
|---|---|---|
| `BufferError` | No se puede realizar una operación sobre un búfer. | `raise BufferError()` |
| `EOFError` | Se alcanza el final de una entrada cuando se esperaba más información. | `raise EOFError()` |
| `MemoryError` | No hay memoria suficiente para completar una operación. | `raise MemoryError()` |

### Importaciones y sintaxis

| Excepción | Definición | Ejemplo |
|---|---|---|
| `ImportError` | Falla una importación. | `from math import funcion_inexistente` |
| `ModuleNotFoundError` | No se encuentra el módulo que se intenta importar. | `import modulo_inexistente` |
| `SyntaxError` | El código tiene una sintaxis incorrecta. | `eval("if True")` |
| `IndentationError` | La indentación del código es incorrecta. | `compile("if True:\nprint(1)", "", "exec")` |
| `TabError` | Se mezclan tabuladores y espacios de forma incompatible en la indentación. | `raise TabError()` |

### Ejecución y funcionamiento interno

| Excepción | Definición | Ejemplo |
|---|---|---|
| `RuntimeError` | Error de ejecución que no encaja en otra categoría específica. | `raise RuntimeError()` |
| `NotImplementedError` | Una operación o método todavía no está implementado. | `raise NotImplementedError()` |
| `RecursionError` | Se supera el límite de llamadas recursivas. | `def f(): return f()`<br/>`f()` |
| `PythonFinalizationError` | Una operación no puede realizarse durante la finalización del intérprete. | `raise PythonFinalizationError()` |
| `SystemError` | Error interno del intérprete. | `raise SystemError()` |

### Iteradores y generadores

| Excepción | Definición | Ejemplo |
|---|---|---|
| `StopIteration` | Indica que un iterador ha terminado. | `next(iter([]))` |
| `StopAsyncIteration` | Indica que un iterador asíncrono ha terminado. | `raise StopAsyncIteration()` |
| `GeneratorExit` | Señala que se solicita cerrar un generador. | `raise GeneratorExit()` |

### Codificación de texto Unicode

| Excepción | Definición | Ejemplo |
|---|---|---|
| `UnicodeError` | Clase base de errores de codificación Unicode. | `raise UnicodeError()` |
| `UnicodeDecodeError` | No se pueden decodificar bytes con una codificación. | `b"\xff".decode("utf-8")` |
| `UnicodeEncodeError` | Un carácter no se puede codificar con la codificación elegida. | `"ñ".encode("ascii")` |
| `UnicodeTranslateError` | Falla una traducción de caracteres Unicode. | `raise UnicodeTranslateError("ñ", 0, 1, "error")` |

### Salida e interrupciones

Estas excepciones heredan directamente de `BaseException`, no de `Exception`. Por eso, un `except Exception` normal no las captura.

| Excepción | Definición | Ejemplo |
|---|---|---|
| `KeyboardInterrupt` | El usuario interrumpe el programa, normalmente con Ctrl+C. | `raise KeyboardInterrupt()` |
| `SystemExit` | Se solicita finalizar el programa. | `raise SystemExit(0)` |

### Advertencias (`Warning`)

Las advertencias informan de situaciones que pueden ser problemáticas, pero no siempre detienen el programa.

| Excepción | Definición | Ejemplo |
|---|---|---|
| `Warning` | Clase base de las advertencias. | `raise Warning("Aviso")` |
| `BytesWarning` | Advierte sobre determinadas operaciones con bytes. | `raise BytesWarning()` |
| `DeprecationWarning` | Una función o característica está obsoleta. | `raise DeprecationWarning()` |
| `PendingDeprecationWarning` | Una característica podría quedar obsoleta en el futuro. | `raise PendingDeprecationWarning()` |
| `SyntaxWarning` | Advierte de una construcción sintáctica sospechosa. | `raise SyntaxWarning()` |
| `RuntimeWarning` | Advierte de una situación sospechosa durante la ejecución. | `raise RuntimeWarning()` |
| `FutureWarning` | Advierte de cambios de comportamiento previstos para los usuarios. | `raise FutureWarning()` |
| `ImportWarning` | Advierte de posibles problemas relacionados con importaciones. | `raise ImportWarning()` |
| `UnicodeWarning` | Advierte de posibles problemas relacionados con Unicode. | `raise UnicodeWarning()` |
| `ResourceWarning` | Advierte de recursos que no se han gestionado correctamente. | `raise ResourceWarning()` |
| `EncodingWarning` | Advierte de posibles problemas relacionados con la codificación predeterminada. | `raise EncodingWarning()` |

### Ejemplo práctico: controlar varios errores

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(resultado)

except ValueError:
    print("Debes introducir un número entero")

except ZeroDivisionError:
    print("El número no puede ser cero")

except Exception as error:
    print("Error inesperado:", error)
```

**Consejo:** captura primero las excepciones específicas y deja `except Exception` para errores inesperados. Evita capturar `BaseException` sin un motivo concreto.

### Referencia oficial

La lista y la jerarquía pueden variar según la versión de Python. Para consultar las excepciones disponibles en tu versión, visita la [documentación oficial de excepciones integradas de Python](https://docs.python.org/3/library/exceptions.html).