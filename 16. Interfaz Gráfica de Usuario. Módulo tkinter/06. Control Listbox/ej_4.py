'''
  Solicitar el ingreso del nombre de una persona y seleccionar de un control Listbox un país. Al presionar un botón
  mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label1 = tk.Label(self.ventana, text="Ingresa tu nombre:")
        self.label1.grid(row=0, column=0)

        self.label2 = tk.Label(self.ventana, text="Selecciona un país:")
        self.label2.grid(row=1, column=0)

        self.nombre = tk.StringVar()

        self.entry = tk.Entry(self.ventana, width=10, textvariable=self.nombre)
        self.entry.grid(row=0, column=1)

        self.pais = tk.StringVar()
        self.listbox = tk.Listbox(self.ventana, listvariable=self.pais)
        self.listbox.grid(row=1, column=1)

        for pais in ["ESP", "FRA", "POR", "ITA"]:
            self.listbox.insert(tk.END, pais)

        self.boton = tk.Button(self.ventana, text="Mostrar datos", command=self.mostrar_datos)
        self.boton.grid(row=2, column=0)

        self.label3 = tk.Label(self.ventana, text="Resultado:")
        self.label3.grid(row=3, column=0)

        self.ventana.mainloop()

    def mostrar_datos(self):
        nombre = self.nombre.get()
        pais = self.listbox.get(self.listbox.curselection())
        self.label3.config(text=f"Nombre: {nombre}\nPaís: {pais}")


Aplicacion()
