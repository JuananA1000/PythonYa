'''
  Confeccionar un programa que tenga solo un menú de opciones que al ser presionado nos muestre un cuadro de mensaje que 
  informe si queremos finalizar la ejecución del programa. Si se presiona "si" se finaliza el programa en caso contrario 
  no se hace nada.
  La representación visual luego de seleccionar la opción del menú es:
'''

import tkinter as tk
from tkinter import messagebox as mb
import sys  # Este módulo proporciona funciones para interactuar con el intérprete de Python.

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Aplicación con Menú de Opciones")

        self.agregar_menu()

        self.ventana.mainloop()

    def agregar_menu(self):
        self.menu_bar = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu_bar)

        self.opciones_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.opciones_menu.add_command(label="Salir", command=self.salir)

        self.menu_bar.add_cascade(label="Opciones", menu=self.opciones_menu)

    def salir(self):
        respuesta = mb.askyesno("Confirmar Salida", "¿Desea finalizar la ejecución del programa?")
        if respuesta:
            sys.exit()  # Finaliza el programa


Aplicacion()
