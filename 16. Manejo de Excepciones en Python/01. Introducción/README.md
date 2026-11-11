## 16.1 Introducción

Las instrucciones `try` y `except` permiten controlar errores y evitar que el programa se detenga inesperadamente.

- `try`: contiene el código que puede provocar un error.
- `except`: ejecuta un código alternativo si ocurre el error indicado.

```python
try:
    numero = int(input("Introduce un número: "))
    print(10 / numero)
except:
    print("Se ha producido un error")
```

### Obtener información del error

Siempre que el operador ingrese valores numéricos solo se ejecuta el bloque del try, pero cuando ingresa un dato no numérico por teclado se genera la excepción 'ValueError' que debe ser capturada despues de except y seguida por el nombre de excepción capturada.

```python
except ValueError:
    print("debe ingresar números.")
```
