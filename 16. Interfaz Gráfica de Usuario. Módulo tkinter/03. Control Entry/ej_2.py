'''
  Confeccionar un programa que permita ingresar el nombre de usuario en un control Entry y cuando se presione un botón 
  mostrar el valor ingresado en la barra de títulos de la ventana.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Aquí se muestra el nombre")

        self.label1 = tk.Label(self.ventana, text="Ingresa tu nombre:")
        self.label1.grid(row=0, column=0)

        self.dato = tk.StringVar()

        self.entry = tk.Entry(self.ventana, width=30, textvariable=self.dato)
        self.entry.grid(row=1, column=0)

        self.boton = tk.Button(self.ventana, text="Mostrar nombre", command=self.mostrar_nombre)
        self.boton.grid(row=2, column=0)

        self.ventana.mainloop()

    def mostrar_nombre(self):
        nombre = self.dato.get()
        self.ventana.title(nombre)


Aplicacion()
