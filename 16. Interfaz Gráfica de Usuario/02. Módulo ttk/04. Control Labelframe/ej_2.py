'''
  Mediante dos controles de tipo LabelFrame implementar la interfaz visual de este vídeo:
  https://youtu.be/4BOawfrcsJ4?si=66mLGBGKJ5f8W4zW
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.lf_art = ttk.LabelFrame(self.ventana, text="Artículo")
        self.lf_art.grid(column=0, row=0, padx=5, pady=10)

        self.articulo()

        self.lf_operaciones = ttk.LabelFrame(self.ventana, text="Operaciones")
        self.lf_operaciones.grid(column=0, row=1, padx=5, pady=10)

        self.operaciones()

        self.ventana.mainloop()

    def articulo(self):
        self.label_cod = ttk.Label(self.lf_art, text="Código de Artículo:")
        self.label_cod.grid(column=0, row=0, padx=4, pady=4)

        self.label_desc = ttk.Label(self.lf_art, text="Descripción:")
        self.label_desc.grid(column=0, row=1, padx=4, pady=4)

        self.label_precio = ttk.Label(self.lf_art, text="Precio:")
        self.label_precio.grid(column=0, row=2, padx=4, pady=4)

        self.entry_cod = ttk.Entry(self.lf_art)
        self.entry_cod.grid(column=1, row=0, padx=4, pady=4)

        self.entry_desc = ttk.Entry(self.lf_art)
        self.entry_desc.grid(column=1, row=1, padx=4, pady=4)

        self.entry_precio = ttk.Entry(self.lf_art)
        self.entry_precio.grid(column=1, row=2, padx=4, pady=4)

    def operaciones(self):
        self.btn_alta = ttk.Button(self.lf_operaciones, text="Alta")
        self.btn_alta.grid(column=0, row=0, padx=4, pady=4)

        self.btn_baja = ttk.Button(self.lf_operaciones, text="Baja")
        self.btn_baja.grid(column=1, row=0, padx=4, pady=4)

        self.btn_modificar = ttk.Button(self.lf_operaciones, text="Modificación")
        self.btn_modificar.grid(column=2, row=0, padx=4, pady=4)


Aplicacion()
