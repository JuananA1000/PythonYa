'''
  Confeccionar una interfaz visual que contenga un menú de opciones que permitan "Guardar archivo", "Recuperar archivo"
  y "Salir del programa".
  En la ventana principal debe aparecer un control de tipo 'scrolledtext' donde el operador pueda escribir un texto para
  luego grabarlo en un archivo de texto. También el control 'scrolledtext' debe cargarse con el contenido de un archivo
  existente en el disco duro.
'''

import sys
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.agregar_menu()

        self.scrolledtext = st.ScrolledText(self.ventana, width=40, height=10)
        self.scrolledtext.grid(row=0, column=0, padx=10, pady=10)

        self.ventana.mainloop()

    def agregar_menu(self):
        menubar = tk.Menu(self.ventana)
        self.ventana.config(menu=menubar)

        opciones = tk.Menu(menubar, tearoff=0)
        opciones.add_command(label="Guardar archivo", command=self.guardar)
        opciones.add_command(label="Recuperar archivo", command=self.recuperar)
        opciones.add_separator()
        opciones.add_command(label="Salir del programa", command=self.salir)
        menubar.add_cascade(label="Archivo", menu=opciones)

    def salir(self):
        sys.exit()

    def guardar(self):
        nombrearch = fd.asksaveasfilename(initialdir="/", title="Guardar como",
                                          filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombrearch != "":
            archivo = open(nombrearch, 'w', encoding='utf-8')
            archivo.write(self.scrolledtext.get("1.0", tk.END))
            archivo.close()
            mb.showinfo("Guardar archivo", "Archivo guardado correctamente.")

    def recuperar(self):
        nombrearch = fd.askopenfilename(initialdir="/", title="Seleccione archivo",
                                        filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombrearch != "":
            archivo = open(nombrearch, 'r', encoding='utf-8')
            contenido = archivo.read()
            archivo.close()
            self.scrolledtext.delete("1.0", tk.END)
            self.scrolledtext.insert(tk.END, contenido)

Aplicacion()