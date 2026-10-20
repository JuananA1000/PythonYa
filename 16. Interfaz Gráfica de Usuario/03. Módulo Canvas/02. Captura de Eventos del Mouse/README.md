### Captura de Eventos del Mouse

Una actividad muy común es poder detectar cuando hemos presionado el mouse dentro de cualquier widget que hayamos visto
y a partir de ahí disparar un evento.

Veremos con una serie de ejemplos la posibilidades que tkinter nos provee.

En Tkinter, puedes asociar acciones del ratón a un widget utilizando el método `.bind()`:

#### Principales secuencias de eventos:

- `<Button-1>` → Clic con el botón izquierdo.
  - `<Button-2>` → Clic con el botón central / rueda.
  - `<Button-3>` → Clic con el botón derecho.
  - `<Double-Button-1>` → Doble clic con el botón izquierdo.
  - `<Motion>` → Movimiento del puntero del ratón sobre el widget.

#### Ejemplo básico de captura de coordenadas (`<Motion>`):

```python
import tkinter as tk


def mover_mouse(evento):
  print(f'Posición del mouse -> X: {evento.x}, Y: {evento.y}')

ventana = tk.Tk()
ventana.geometry('300x200')
ventana.bind('<Motion>', mover_mouse) # Asociar el movimiento del mouse en la ventana a la función
ventana.mainloop()
```
