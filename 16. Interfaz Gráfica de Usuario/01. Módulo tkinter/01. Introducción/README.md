## Introducción

Al instalar Python en nuestro equipo, por defecto instala el módulo **tkinter** para la implementación de interfaces visuales.

Ejemplo: *Mostrar una ventana y que en su título aparezca el mensaje 'Hola Mundo'*.

```python

import tkinter as tk # Importamos el módulo tkinter y le definimos un alias
ventana1 = tk.Tk() # Creamos un objeto de la clase Tk
ventana1.title("Hola Mundo") # Le pasamos un string con el mensaje que queremos que aparezca en la barra del título de la ventana
ventana1.mainloop() # Llamamos al método 'mainloop' que pertenece a la clase Tk
```

### Aplicación Orientada a Objetos

En todos los ejemplos que haremos de ahora utilizaremos la metodología de POO (Programación Orientada a Objetos)

Ejemplo: *El programa anterior modificado con POO sería:*.

```python
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Hola Mundo")
        self.ventana1.mainloop()


aplicacion1 = Aplicacion()
```

En este ejemplo planteamos una clase llamada 'Aplicacion' y en su método '__init__' creamos el objeto de la clase 'Tk' para que se muestre la ventana.

Debemos crear luego un objeto de la clase 'Aplicacion':

```python
aplicacion1 = Aplicacion()
```
