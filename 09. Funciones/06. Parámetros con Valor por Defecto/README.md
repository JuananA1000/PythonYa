## Parámetros con Valor por Defecto

En Python se pueden definir parámetros con valores en la misma cabecera de la función. Cuando llamemos a la función podemos o no enviarle un valor distinto al parámetro.

Los parámetros por defecto permiten crear **funciones más flexibles** y emplearlas en distintas circunstancias.

Ejemplo: *Función con un parámetro con un valor por defecto*:
```python
def saludar(nombre="Juan"):
    return f"Hola, {nombre}!"

print(saludar())         # Salida: Hola, Juan!
print(saludar("Paco"))   # Salida: Hola, Paco!
```

Si llamamos a la función `saludar()` sin argumentos, **usará el valor por defecto** (en este caso, 'Juan').

> [!IMPORTANT]  
> Los parámetros por defecto deben ser los **últimos que se declaren en la función**. Se genera un error si definimos una función con los valores por defecto al principio, por lo que:
>
> esto es INCORRECTO:
> ```python
> def suma(num1=4, num2=3, num3=7, num4, num5):
> ```
>
> esto es CORRECTO:
> ```python
>  def suma(num1, num2, num3=4, num4=3, num5=7):`
> ```