'''
  Solicitar el ingreso del nombre de una persona y seleccionar de un control Combobox un país. Al presionar un botón 
  mostrar en la barra de la ventana el nombre ingresado y el país seleccionado. 
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Selector de Países")

        self.label_nombre = tk.Label(self.ventana, text="Ingrese su nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.paises = ["ESP", "FRA", "POR", "ITA"]

        self.combobox_paises = ttk.Combobox(self.ventana, values=self.paises)
        self.combobox_paises.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.boton_mostrar = tk.Button(self.ventana, text="Mostrar datos", command=self.mostrar_datos)
        self.boton_mostrar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.ventana.mainloop()

    def mostrar_datos(self):
        nombre = self.entry_nombre.get()
        pais_seleccionado = self.combobox_paises.get()
        self.ventana.title(f"{nombre} - {pais_seleccionado}")


Aplicacion()
