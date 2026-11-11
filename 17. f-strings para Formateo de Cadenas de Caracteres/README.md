# 20. f-strings Para Formateo de Cadenas de Caracteres

Las **f-strings** (formatted string literals) permiten insertar variables, expresiones y operaciones en una cadena de texto. Son una herramienta fundamental de Python. Permiten generar textos dinámicos, mostrar resultados numéricos y construir mensajes de forma sencilla y legible.

Se identifican colocando `f` delante de las comillas `""` y utilizando llaves `{}` para introducir la variable que queremos mostrar.

## Inserción de variables

Podemos insertar directamente variables dentro de una cadena:

```python
nombre = "Juan"
edad = 32

print(f"Me llamo {nombre} y tengo {edad} años.")
```

## Inserción de expresiones

También podemos introducir operaciones matemáticas y expresiones directamente dentro de las llaves:

```python
precio = 25
unidades = 3

print(f"El precio total es {precio * unidades} euros.")
```

## Formateo de números decimales

Podemos controlar el número de decimales utilizando `:.nf`, donde `n` representa la cantidad de decimales.

```python
precio = 23.5678

print(f"Precio: {precio:.2f}")  # 23.57
print(f"Precio: {precio:.1f}")  # 23.6
print(f"Precio: {precio:.0f}")  # 24
```

## Separadores de miles

Podemos utilizar `:,` para separar los miles mediante comas:

```python
numero = 1500000

print(f"{numero:,}")  # 1,500,000
```

También podemos combinarlo con los decimales:

```python
precio = 1234567.891

print(f"{precio:,.2f}")  # 1,234,567.89
```

## Alineación del texto

Podemos establecer la alineación del contenido dentro de un espacio determinado:

- `<` : Alineación izquierda.
- `>` : Alineación derecha.
- `^` : Alineación centrada.

```python
nombre = "Juan"

print(f"{nombre:<15}")  # Juan           
print(f"{nombre:>15}")  #            Juan
print(f"{nombre:^15}")  #      Juan     
```

También podemos utilizar caracteres personalizados para rellenar los espacios:

```python
print(f"{nombre:*^15}")  # ******Juan*****
```

## Rellenar números con ceros

Podemos establecer una longitud determinada y rellenar los espacios sobrantes con ceros:

```python
numero = 25

print(f"{numero:05d}")  # 00025
print(f"{numero:08d}")  # 00000025
```

## Porcentajes

Podemos representar valores decimales como porcentajes utilizando `%`:

```python
porcentaje = 0.8567

print(f"{porcentaje:.2%}") # 85.67%
```

## Mostrar llaves literales

Si queremos mostrar las llaves `{}` como caracteres normales, debemos duplicarlas:

```python
nombre = "Juan"

print(f"{{Hola {nombre}}}") # {Hola Juan}
```

## Depuración de variables

Podemos utilizar `=` dentro de una f-string para mostrar el nombre de una variable y su valor:

```python
edad = 32
precio = 25.50

print(f"{edad=}") # edad=32
print(f"{precio=}") # precio=25.5
```

## Resumen de formatos

| Formato | Función |
|---|---|
| `{variable}` | Insertar una variable |
| `{expresion}` | Evaluar una expresión |
| `{numero:.2f}` | Mostrar dos decimales |
| `{numero:,}` | Separar los miles con comas |
| `{texto:<15}` | Alinear a la izquierda |
| `{texto:>15}` | Alinear a la derecha |
| `{texto:^15}` | Centrar el contenido |
| `{numero:05d}` | Rellenar con ceros |
| `{numero:.2%}` | Mostrar un porcentaje |
| `{{ }}` | Mostrar llaves literales |
| `{variable=}` | Mostrar nombre y valor de una variable |
