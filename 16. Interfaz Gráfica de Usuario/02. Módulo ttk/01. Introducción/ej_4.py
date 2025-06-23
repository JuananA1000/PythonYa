'''
  Mostrar una ventana y en su interior tres controles de tipo Checkbutton cuyas etiquetas correspondan a distintos 
  lenguajes de programación. Cuando se presione un botón mostrar en una Label la cantidad de Checkbutton que se 
  encuentran chequeados. Utilizar Widget del módulo ttk.
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label = ttk.Label(self.ventana, text="Selecciona los lenguajes de programación:")
        self.label.grid(row=0, column=1, padx=10, pady=10)

        self.seleccionados = []

        self.checkbutton_python = ttk.Checkbutton(self.ventana, text="Python")
        self.checkbutton_python.grid(row=1, column=0, padx=10, pady=10)

        self.checkbutton_java = ttk.Checkbutton(self.ventana, text="Java")
        self.checkbutton_java.grid(row=1, column=1, padx=10, pady=10)

        self.checkbutton_csharp = ttk.Checkbutton(self.ventana, text="C#")
        self.checkbutton_csharp.grid(row=1, column=2, padx=10, pady=10)

        self.boton_actualizar = ttk.Button(self.ventana, text="Actualizar", command=self.actualizar_label)
        self.boton_actualizar.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.resultado_label = ttk.Label(self.ventana, text="")
        self.resultado_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.ventana.mainloop()

    def actualizar_label(self):
        contador = 0

        if self.checkbutton_python.instate(['selected']):
            contador += 1
        if self.checkbutton_java.instate(['selected']):
            contador += 1
        if self.checkbutton_csharp.instate(['selected']):
            contador += 1

        self.resultado_label.config(text=f"Cantidad de lenguajes seleccionados: {contador}")


Aplicacion()
