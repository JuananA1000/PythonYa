### Mostrar una Imagen

Si necesitamos mostrar una imagen dentro de un Canvas utilizaremos el método `PhotoImage` de tkinter, y luego mediante el método `create_image()` de la clase Canvas para su visualización.

#### Método `PhotoImage()`

Permite cargar una imagen para utilizarla en una interfaz gráfica de Tkinter.

**Sintaxis:**

```python
imagen = tk.PhotoImage(file="imagen.png")
```

- `file`: ruta del archivo de imagen.

Admite formatos como **.png** y **.gif**, entre otros. Para cargar imágenes .jpg, se puede utilizar la biblioteca Pillow.

#### Método `create_image()`

Permite mostrar una imagen dentro de un `Canvas`.

**Sintaxis:**

```python
canvas.create_image(x, y, image=imagen)
```

- `x`, `y`: coordenadas donde se coloca la imagen. Por defecto, indican su centro.
- `image`: objeto de imagen previamente cargado con `PhotoImage()`.

#### Ejemplo completo

```python
import tkinter as tk
from pathlib import Path

ventana = tk.Tk()

canvas = tk.Canvas(ventana, width=400, height=300)
canvas.pack()

# Cargar la imagen desde la carpeta del script
ruta = Path(__file__).parent / "carta1.png"
img1 = tk.PhotoImage(file=ruta)

# Mostrar la imagen en el Canvas
canvas.create_image(200, 150, image=img1)

ventana.mainloop()
```

**Importante:** conserva una referencia a la imagen (`img1`) mientras se esté utilizando. Si se elimina la referencia, la imagen podría dejar de mostrarse.