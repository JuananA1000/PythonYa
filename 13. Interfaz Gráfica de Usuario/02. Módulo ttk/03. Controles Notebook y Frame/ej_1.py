'''
  Confeccionar una aplicación que muestre un cuaderno con tres pestañas. Los títulos de cada pestaña deben ser 'Button', 
  'Label' y 'Entry'. Según la pestaña seleccionada mostrar un mensaje informando el objetivo de la clase y un ejemplo de 
  la misma.
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejemplo de Notebook")

        # Crear el Notebook
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(expand=True, fill='both')

        # Pestaña Button
        self.pestana_button = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_button, text='Button')
        self.label_button = tk.Label(self.pestana_button, text="Objetivo: Mostrar un botón.\nEjemplo:")
        self.label_button.pack(pady=10)
        self.button_example = tk.Button(self.pestana_button, text="Botón de ejemplo")
        self.button_example.pack(pady=10)

        # Pestaña Label
        self.pestana_label = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_label, text='Label')
        self.label_label = tk.Label(self.pestana_label, text="Objetivo: Mostrar una etiqueta.\nEjemplo:")
        self.label_label.pack(pady=10)
        self.label_example = tk.Label(self.pestana_label, text="Etiqueta de ejemplo")
        self.label_example.pack(pady=10)

        # Pestaña Entry
        self.pestana_entry = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_entry, text='Entry')
        self.label_entry = tk.Label(self.pestana_entry, text="Objetivo: Mostrar un campo de entrada.\nEjemplo:")
        self.label_entry.pack(pady=10)
        self.entry_example = tk.Entry(self.pestana_entry)
        self.entry_example.pack(pady=10)

        self.ventana.mainloop()

Aplicacion()  