# 08. Estructuras de Datos

Python dispone de diferentes estructuras de datos que permiten almacenar y organizar información. Las principales son las **listas, tuplas, diccionarios y conjuntos (set)**.

## Listas (`list`)

Permiten almacenar varios elementos en una misma variable. Son **ordenadas, modificables y permiten elementos duplicados**.

```python
frutas = ["manzana", "pera", "naranja", "pera"]

print(frutas[0])  # Acceder a un elemento mediante su índice
frutas[1] = "plátano" # Modificar un elemento
frutas.append("kiwi") # Añadir un elemento
frutas.remove("naranja") # Eliminar un elemento

```

## Tuplas (`tuple`)

Similares a las listas, tienen la característica fundamental de ser **inmutables**, es decir, no permiten modificar, añadir ni eliminar elementos.

Son ordenadas y **permiten duplicados**.

```python
coordenadas = (10, 20, 30)

print(coordenadas[0])  # Acceder a un elemento

for coordenada in coordenadas: # Recorrer una tupla
    print(coordenada)

coordenadas[0] = 50  # Generaría un error porque no se pueden modificar sus elementos
```

## Diccionarios (`dict`)

Permiten almacenar datos mediante pares de **clave y valor**. Cada clave debe ser única y permite acceder directamente al valor asociado.

Son modificables y mantienen el orden de inserción.

```python
persona = {
    "nombre": "Juan",
    "edad": 32,
    "ciudad": "Madrid"
}

print(persona["nombre"]) # Acceder a un valor mediante su clave
persona["edad"] = 33 # Modificar un valor
persona["profesion"] = "Programador" # Añadir un nuevo par clave-valor
del persona["ciudad"] # Eliminar un elemento
```

## Conjuntos (`set`)

Permiten almacenar elementos **únicos**, luego **no admiten duplicados**. No mantienen un orden de inserción garantizado y no permiten acceder a sus elementos mediante índices.

Son modificables y resultan especialmente útiles para eliminar duplicados y realizar operaciones matemáticas entre conjuntos.

```python
numeros = {1, 2, 3, 4, 4, 5}

print(numeros)  # Los elementos duplicados desaparecen
numeros.add(6) # Añadir un elemento
numeros.remove(3) # Eliminar un elemento

# Operaciones entre conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Unión: {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersección: {3, 4}
print(a - b)  # Diferencia: {1, 2}
```

> [!IMPORTANT]
> Para crear un conjunto vacío se utiliza `set()`, ya que `{}` crea un diccionario vacío.

## Diferencias entre las estructuras de datos

| Característica    | Lista | Tupla | Diccionario      | Set  |
| ----------------- | ----- | ----- | ---------------- | ---- |
| Sintaxis          | `[]`  | `()`  | `{clave: valor}` | `{}` |
| Ordenada          | Sí    | Sí    | Sí               | No   |
| Modificable       | Sí    | No    | Sí               | Sí   |
| Admite duplicados | Sí    | Sí    | Claves no        | No   |
| Acceso por índice | Sí    | Sí    | No               | No   |
| Acceso por clave  | No    | No    | Sí               | No   |

## ¿Cuándo utilizar cada una?

- **Listas:** cuando necesitamos almacenar varios elementos y modificar su contenido.
- **Tuplas:** cuando queremos almacenar datos que no deberían modificarse.
- **Diccionarios:** cuando necesitamos relacionar claves con valores y acceder a ellos mediante una clave identificativa.
- **Conjuntos (set):** cuando necesitamos almacenar elementos únicos o realizar operaciones de unión, intersección y diferencia.
