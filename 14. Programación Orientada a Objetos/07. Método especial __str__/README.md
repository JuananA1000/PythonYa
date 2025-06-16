## Método especial __str__

Si llamamos a la función `print()` y le pasamos como parámetro un objeto...

```python
class Persona:
    def __init__(self,nom,ape):
        self.nombre = nom
        self.apellido = ape
 
persona1 = Persona("Jose","Rodriguez")
print(persona1)
```

...Nos muestra algo parecido a esto:

```python
<__main__.Persona object at 0x03E99C90>
```

Para mostrar el nombre y apellido separados por coma cuando llamemos a la función `print()` en el código anterior, que debemos definir en la clase el método especial `__str__` y retornar un string, eel cual, luego se imprimirá con la función `print()`:

```python
class Persona:
    def __init__(self,nom,ape):
        self.nombre = nom
        self.apellido = ape

    def __str__(self):
        cadena = self.nombre + "," + self.apellido

        return cadena
 
persona1 = Persona("Jose","Rodriguez")
print(persona1)
```

Esta característica definida en Python nos permite crear programas muy legibles y flexibles.

El método `__str__` también se ejecuta si llamamos a la función `str()` y pasamos como parámetro un objeto que tiene definido dicho método:

```python
class Persona:
    def __init__(self,nom,ape):
        self.nombre = nom
        self.apellido = ape

    def __str__(self):
        cadena = self.nombre + "," + self.apellido
        return cadena

persona1 = Persona("Jose","Rodriguez")
persona2 = Persona("Ana","Martinez")
print(str(persona1) + "-" + str(persona2))  # Jose,Rodriguez-Ana,Martinez 
```