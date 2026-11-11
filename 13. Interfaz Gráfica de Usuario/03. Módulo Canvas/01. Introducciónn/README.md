### Introducción

El control Canvas nos permite dibujar figuras como líneas, rectángulos, óvalos, arcos, etc.

```python
import tkinter as tk
```

#### create_line()

Dibuja una línea entre uno o varios puntos.

* `fill` → color de relleno inicial.
* `width` → grosor de la línea.

```python
canvas.create_line(x1, y1, x2, y2, ...)

canvas.create_line(50, 50, 300, 150, fill="red", width=3) # Ejemplo de código
```
---

#### create_rectangle()

Dibuja un rectángulo indicando sus esquinas superior izquierda e inferior derecha.

```python
canvas.create_rectangle(x1, y1, x2, y2)

canvas.create_rectangle(
    50, 50, 250, 150,
    fill="blue",
    outline="black",
    width=2
) # Ejemplo de código
```
---

#### create_oval()

Dibuja un óvalo inscrito **dentro de un rectángulo** definido por coordenadas.

```python
canvas.create_oval(x1, y1, x2, y2)

#Si el ancho y el alto son iguales, obtenemos un círculo.
canvas.create_oval(
    50, 50, 200, 200,
    fill="green"
) # Ejemplo de código
```
---

#### create_polygon()

Dibuja un polígono conectando una serie de puntos.

```python
canvas.create_polygon(x1, y1, x2, y2, ...)

canvas.create_polygon(
    100, 50,
    50, 150,
    150, 150,
    fill="orange"
) # Ejemplo de código
```
---

#### create_arc()

Dibuja un arco basado en una elipse.

* `start` → ángulo inicial.
* `extent` → amplitud del arco.
* `style` → tipo de arco.

```python
canvas.create_arc(
    x1, y1, x2, y2,
    start=0,
    extent=180
)

canvas.create_arc(
    50, 50, 250, 250,
    start=0,
    extent=180,
    style="arc",
    outline="purple",
    width=3
) # Ejemplo de código
```