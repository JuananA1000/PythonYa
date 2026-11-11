## 8.5 Compresión de Listas

La compresión de listas nos permite crear listas a partir de otras listas, tuplas y cualquier iterable.

Permite escribir en una sola línea operaciones que normalmente necesitarían un bucle `for`.

### Sintaxis básica

```python
nueva_lista = [expresion for elemento in iterable]
```

- `expresion`: operación que se realiza con cada elemento.
- `elemento`: variable que representa cada elemento.
- `iterable`: colección sobre la que se itera.

*Ejemplo:*
```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [n ** 2 for n in numeros]

print(cuadrados) # [1, 4, 9, 16, 25]
```

### Compresión de listas con condiciones

Podemos añadir una condición `if` para seleccionar únicamente los elementos que cumplan determinados requisitos.

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = [n for n in numeros if n % 2 == 0]

print(pares) # [2, 4, 6, 8]
```

### Modificar elementos y aplicar condiciones

También podemos combinar operaciones y condiciones.

```python
numeros = [1, 2, 3, 4, 5, 6]
cuadrados_pares = [n ** 2 for n in numeros if n % 2 == 0]

print(cuadrados_pares) # [4, 16, 36]
```

### Condicional `if-else`

Podemos utilizar `if-else` para decidir qué valor introducir en la nueva lista.

En este caso, el condicional se coloca antes del `for`.

```python
numeros = [1, 2, 3, 4, 5]
resultado = ["Par" if n % 2 == 0 else "Impar" for n in numeros]

print(resultado) # ['Impar', 'Par', 'Impar', 'Par', 'Impar']
```

### Equivalencia con un bucle for

La compresión de listas permite simplificar código convencional.

*Ejemplo con un bucle for:*
```python
numeros = [1, 2, 3, 4, 5]
cuadrados = []

for n in numeros:
    cuadrados.append(n ** 2)
```

*Con compresión de listas:*
```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [n ** 2 for n in numeros]
```

### Compresión de listas anidadas

También podemos utilizar varios bucles `for` dentro de una misma compresión.

```python
pares = [(x, y) for x in [1, 2] for y in [3, 4]]

print(pares) # [(1, 3), (1, 4), (2, 3), (2, 4)]
```