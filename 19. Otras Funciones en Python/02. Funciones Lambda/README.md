## 02. Funciones Lambda

Las **funciones lambda** son funciones anónimas que permiten definir pequeñas operaciones en una sola expresión, sin necesidad de utilizar `def`.

### Sintaxis

```python
lambda argumentos: expresion
```

- `lambda`: palabra reservada para crear la función.
- `argumentos`: parámetros que recibe.
- `expresion`: operación cuyo resultado devuelve automáticamente.

*Ejemplo de código: función tradicional*
```python
def sumar(a, b): # Función tradicional
    return a + b

sumar = lambda a, b: a + b # Función lambda equivalente

print(sumar(5, 3)) # 8
```

Estas funciones no necesitan `return`, ya que devuelven automáticamente el resultado de su expresión.

### Utilizar Lambda con funciones de orden superior

Una de las principales ventajas de lambda es que permite definir funciones directamente donde se necesitan, sin tener que declararlas previamente.

#### `map()`

_Ejemplo de código: multiplica por 2 todos los elementos de esta lista_
```python
numeros = [1, 2, 3, 4, 5]

resultado = map(lambda n: n * 2, numeros)

print(list(resultado)) # [2, 4, 6, 8, 10]
```
#### `filter()`

_Ejemplo de código: devuelve todos los elementos pares_
```python
numeros = [1, 2, 3, 4, 5, 6]

resultado = filter(lambda n: n % 2 == 0, numeros)

print(list(resultado)) # [2, 4, 6]
```

#### `sorted()`

_Ejemplo de código: ordena de menor a mayor los nombres de las personas, atendiendo a sus edades_
```python
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 18},
    {"nombre": "Carlos", "edad": 32}
]

resultado = sorted(personas, key=lambda persona: persona["edad"])

print(resultado) # En este caso la ordenación se realiza utilizando las edades.
```

