'''
  Mostrar dos Label, en una se muestra el nombre del programa y en la segunda el año de creación. Disponer un botón para 
  finalizar el programa.
  No permitir al usuario redimensionar la ventana.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Mi Aplicación")
        self.ventana.geometry("300x200")
        self.ventana.resizable(False, False)

        self.label_nom = tk.Label(self.ventana, text=f"Nombre del Programa: {self.ventana.title()}")
        self.label_nom.pack()

        self.label_age = tk.Label(self.ventana, text="Año de Creación: 2025")
        self.label_age.pack()

        self.boton = tk.Button(self.ventana, text="Salir", command=self.ventana.quit)
        self.boton.pack()

        self.ventana.mainloop()


Aplicacion()
