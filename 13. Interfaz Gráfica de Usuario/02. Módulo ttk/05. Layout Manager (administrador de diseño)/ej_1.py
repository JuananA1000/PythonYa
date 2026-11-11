'''
  Disponer una serie de botones utilizando el Layout Manager de tipo Pack.
  La representación visual debe ser:
'''

import tkinter as tk
from tkinter import ttk


class Aplicacion(tk.Tk):
    def __init__(self):
        self.ventana = tk.Tk()

        self.ventana.title("Ejemplo de Layout Manager Pack")

        self.btn1 = ttk.Button(self.ventana, text="Botón 1")
        self.btn1.pack(side=tk.TOP, fill=tk.BOTH)

        self.btn2 = ttk.Button(self.ventana, text="Botón 2")
        self.btn2.pack(side=tk.TOP, fill=tk.BOTH)

        self.btn3 = ttk.Button(self.ventana, text="Botón 3")
        self.btn3.pack(side=tk.TOP, fill=tk.BOTH)

        self.btn4 = ttk.Button(self.ventana, text="Botón 4")
        self.btn4.pack(side=tk.LEFT)

        self.btn5 = ttk.Button(self.ventana, text="Botón 5")
        self.btn5.pack(side=tk.RIGHT)

        self.btn6 = ttk.Button(self.ventana, text="Botón 6")
        self.btn6.pack(side=tk.RIGHT)

        self.btn7 = ttk.Button(self.ventana, text="Botón 7")
        self.btn7.pack(side=tk.RIGHT)

        self.ventana.mainloop()


Aplicacion()
