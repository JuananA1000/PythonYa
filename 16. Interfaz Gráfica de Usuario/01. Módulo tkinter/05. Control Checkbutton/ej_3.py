'''
  Disponer varios objetos de la clase Checkbutton con nombres de navegadores web. En el título de la ventana mostrar 
  todos los nombres de navegadores seleccionados.
'''

import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Navegadores Web Seleccionados")

        self.check_vars = {
            "Chrome": tk.IntVar(),
            "Firefox": tk.IntVar(),
            "Safari": tk.IntVar(),
            "Edge": tk.IntVar()
        }

        for i, (nombre, var) in enumerate(self.check_vars.items()):
            checkbutton = tk.Checkbutton(self.ventana, text=nombre, variable=var, command=self.actualizar_titulo)
            checkbutton.grid(row=i, column=0, padx=10, pady=5)

        self.ventana.mainloop()

    def actualizar_titulo(self):
        navegadores_seleccionados = [nombre for nombre, var in self.check_vars.items() if var.get() == 1]
        titulo = navegadores_seleccionados
        self.ventana.title(titulo)


Aplicacion()
