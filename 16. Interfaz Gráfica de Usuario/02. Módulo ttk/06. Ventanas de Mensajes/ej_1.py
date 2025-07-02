'''
  Confeccionar una aplicación que permita ingresar dos valores enteros y al presionar un botón nos muestre la suma en el 
  título de la ventana. Si el operador no ingresa en alguno de los dos controles Entry datos informar mediante un 
  diálogo el error que se está cometiendo.
  Agregar además un menú de opciones que al ser seleccionado nos muestre información del programa.
  La representación visual cuando se presiona el botón "sumar" y no se ingresa alguno de los dos números debe ser:
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.labelframe = ttk.LabelFrame(self.ventana, text="Suma de números")
        self.labelframe.grid(column=0, row=0, padx=10, pady=10)

        self.agregar_componentes()
        self.agregar_menu()

        self.ventana.mainloop()

    def agregar_componentes(self):
        self.label_num1 = ttk.Label(self.labelframe, text="Número 1:")
        self.label_num1.grid(column=0, row=0, padx=5, pady=5)

        self.entry_num1 = ttk.Entry(self.labelframe)
        self.entry_num1.grid(column=1, row=0, padx=5, pady=5)

        self.label_num2 = ttk.Label(self.labelframe, text="Número 2:")
        self.label_num2.grid(column=0, row=1, padx=5, pady=5)

        self.entry_num2 = ttk.Entry(self.labelframe)
        self.entry_num2.grid(column=1, row=1, padx=5, pady=5)

        self.boton_sumar = ttk.Button(self.labelframe, text="Sumar", command=self.sumar)
        self.boton_sumar.grid(column=0, row=2, columnspan=2, padx=5, pady=5)

    def agregar_menu(self):
        self.menu_bar = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu_bar)

        self.opciones_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.opciones_menu.add_command(label="Acerca de...", command=self.acerca_de)

        self.menu_bar.add_cascade(label="Opciones", menu=self.opciones_menu)

    def sumar(self):
        num1 = self.entry_num1.get()
        num2 = self.entry_num2.get()

        if not num1 or not num2:
            mb.showerror("Error", "Por favor, ingrese ambos números.")
            return
        else:
            resultado = int(num1) + int(num2)
            self.ventana.title(f"Suma: {resultado}")

    def acerca_de(self):
        mb.showinfo("Acerca de", "Aplicación para sumar dos números enteros.\nDesarrollada por JuananA1000.\nVersión 1.0")


Aplicacion()
