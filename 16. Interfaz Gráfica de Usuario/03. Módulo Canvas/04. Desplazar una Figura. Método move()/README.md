### Desplazar una Figura. Método `move()`

Otra situación donde utilizaremos el id de una figura es cuando queramos desplazarla a otra posición dentro del Canvas.

El método `move()` permite desplazar un elemento dibujado en un `Canvas` de Tkinter, ya sea un cuadrado, círculo, línea o imagen.

#### Sintaxis

```python
canvas.move(elemento, dx, dy)
```

- **`elemento`**: identificador (`id`) de la figura que queremos mover. También puede ser una etiqueta (`tag`) que agrupe varios elementos.
- **`dx`**: desplazamiento horizontal en píxeles. Los valores positivos mueven el elemento hacia la derecha y los negativos hacia la izquierda.
- **`dy`**: desplazamiento vertical en píxeles. Los valores positivos lo mueven hacia abajo y los negativos hacia arriba.

#### Ejemplos

```python
# Mover el cuadrado 10 píxeles a la derecha
canvas.move(cuadrado, 10, 0)

# Moverlo 10 píxeles hacia arriba
canvas.move(cuadrado, 0, -10)

# Moverlo 5 píxeles a la izquierda y 5 hacia abajo
canvas.move(cuadrado, -5, 5)
```

#### Movimiento mediante el teclado

Podemos combinar `move()` con los eventos del teclado para controlar una figura. Por ejemplo:

```python
def pulsar_tecla(self, evento):
    if evento.keysym == 'Right':
        self.canvas.move(self.cuadrado, 4, 0)
    elif evento.keysym == 'Left':
        self.canvas.move(self.cuadrado, -4, 0)
```

En este caso, cada vez que se pulsa la flecha derecha, el cuadrado avanza 4 píxeles hacia la derecha; con la flecha izquierda, retrocede 4 píxeles.

#### Diferencia entre `move()` y `coords()`

- **`move()`** desplaza una figura respecto a su posición actual.
- **`coords()`** permite consultar o establecer las coordenadas de una figura.

Por ejemplo, `canvas.coords(cuadrado)` devuelve las coordenadas actuales del cuadrado, mientras que `canvas.move(cuadrado, 4, 0)` lo desplaza 4 píxeles hacia la derecha.

**Importante:** `move()` no comprueba los límites del Canvas. Si queremos impedir que una figura salga del área visible, debemos comprobar previamente sus coordenadas con `coords()`.