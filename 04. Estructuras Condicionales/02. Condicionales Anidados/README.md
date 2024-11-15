# Estructuras Condicionales Anidadas

Hablamos de **Estructuras Condicionales Anidadas** cuando, por cualquier de una estructura condicional, hay **otra estructura condicional, de nivel inferior**.

![Estructura Condicional Anidada](https://github.com/JuananA1000/PythonYa/blob/main/04.%20Estructuras%20Condicionales/02.%20Condicionales%20Anidados/ECA.jpg?raw=true)

El esquema básico de este tipo de estructuras sería este...:

```python
if condition:
    # code
else:
    if condition:
        # code
    else:
        # code
```

o este...:

```python
if condition:
    if condition:
        # code
    else:
        # code
else:
    # code
```

> [!IMPORTANT]  
> En este tipo de condicionales puede haber **muchos niveles** aunque, generalmente, **no es un código eficiente**.