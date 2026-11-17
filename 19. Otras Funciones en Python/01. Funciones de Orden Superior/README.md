## 19.1 Funciones de Orden Superior

Una **Función de Orden Superior** es aquella que cumple _al menos una_ de estas condiciones:

- Recibe otra función como argumento.
- Devuelve otra función como resultado.

Esto permite reutilizar código y crear funciones más flexibles y dinámicas.

_Ejemplo: recibir una función como argumento_
```python
def operar(funcion, a, b):
    return funcion(a, b)

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

print(operar(sumar, 5, 3))       # 8
print(operar(multiplicar, 5, 3)) # 15
```

La función `operar()` recibe otra función como argumento y la ejecuta.

### Funciones de Orden Superior integradas en Python

Python incorpora varias Funciones de Orden Superior especialmente útiles:

#### `map()`

_Ejemplo: Aplica una función a cada elemento de un iterable y devuelve un iterador con los resultados._
```python
numeros = [1, 2, 3, 4, 5]

def duplicar(numero):
    return numero * 2

resultado = map(duplicar, numeros)

print(list(resultado)) # [2, 4, 6, 8, 10]
```

#### `filter()`

_Ejemplo: Filtra los elementos de un iterable según una condición. Solo conserva aquellos para los que la función devuelve `True`._
```python
numeros = [1, 2, 3, 4, 5, 6]

def es_par(numero):
    return numero % 2 == 0

resultado = filter(es_par, numeros)

print(list(resultado))# [2, 4, 6]
```

#### `sorted()`

_Ejemplo: Ordena los elementos de un iterable. Permite utilizar el parámetro `key` para indicar una función que determine el criterio de ordenación._
```python
palabras = ["Python", "Java", "C", "JavaScript"]

resultado = sorted(palabras, key=len)

print(resultado) # ['C', 'Java', 'Python', 'JavaScript']
```
