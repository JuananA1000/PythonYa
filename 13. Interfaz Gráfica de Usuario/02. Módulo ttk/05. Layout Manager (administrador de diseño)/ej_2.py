'''
  Disponer una serie de botones utilizando el Layout Manager de tipo Grid.
  La representación visual debe ser:
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.btn1 = ttk.Button(self.ventana, text="Botón 1")
        self.btn1.grid(row=0, column=0)

        self.btn2 = ttk.Button(self.ventana, text="Botón 2")
        self.btn2.grid(row=0, column=1)

        self.btn3 = ttk.Button(self.ventana, text="Botón 3")
        self.btn3.grid(row=0, column=2, rowspan=2, sticky="ns")  # que el botón se expanda de Norte a Sur

        self.btn4 = ttk.Button(self.ventana, text="Botón 4")
        self.btn4.grid(row=1, column=0)

        self.btn5 = ttk.Button(self.ventana, text="Botón 5")
        self.btn5.grid(row=1, column=1)

        self.btn6 = ttk.Button(self.ventana, text="Botón 6")
        self.btn6.grid(row=2, column=0, columnspan=3, sticky="we")  # que el botón se expanda de Este a Oeste
        # NOTA: La prop column se puede eliminar, ya que por defecto es 0

        self.ventana.mainloop()


Aplicacion()
