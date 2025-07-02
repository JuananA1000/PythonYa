'''
  Disponer dos botones en la parte inferior derecha de la ventana utilizando el Layout Manager de tipo Place. El ancho y 
  alto de la ventana debe ser de 800 por 600 píxeles.
  La representación visual debe ser:
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("800x600")

        self.boton1 = ttk.Button(self.ventana, text="Botón 1")
        self.boton1.place(x=700, y=550)

        self.boton2 = ttk.Button(self.ventana, text="Botón 2")
        self.boton2.place(x=600, y=550)

        self.ventana.mainloop()


Aplicacion()
