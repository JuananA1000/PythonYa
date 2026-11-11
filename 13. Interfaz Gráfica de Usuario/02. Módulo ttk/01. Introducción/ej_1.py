'''
  Mostrar una ventana y en su interior dos botones y una label utilizando el módulo ttk. La label muestra inicialmente 
  el valor 1. Cada uno de los botones permiten incrementar o decrementar en uno el contenido de la label
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Contador")
        self.valor = 1

        self.label = ttk.Label(self.ventana, text=self.valor)
        self.label.grid(column=0, row=0)
        self.label.configure(foreground="red")

        self.btn_mas = ttk.Button(self.ventana, text="Incrementar", command=self.incrementar)
        self.btn_mas.grid(column=0, row=1)

        self.btn_min = ttk.Button(self.ventana, text="Decrementar", command=self.decrementar)
        self.btn_min.grid(column=0, row=2)

        self.ventana.mainloop()

    def incrementar(self):
        self.valor += 1
        self.label.config(text=str(self.valor))

    def decrementar(self):
        self.valor -= 1
        self.label.config(text=str(self.valor))


Aplicacion()
