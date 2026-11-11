'''
  Mediante dos controles de tipo Entry permitir el ingreso de dos números. Crear un menú que contenga una opción que 
  cambie el tamaño de la ventana con los valores ingresados por teclado. Finalmente disponer otra opción que finalice el 
  programa 
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejemplo de Menú")

        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)

        # Submenú para cambiar el tamaño de la ventana
        opcion_tamano = tk.Menu(barra_menu)
        opcion_tamano.add_command(label="Cambiar Tamaño", command=self.cambiar_tamano)
        barra_menu.add_cascade(label="Tamaño", menu=opcion_tamano)

        # Opción para salir del programa
        barra_menu.add_command(label="Salir", command=self.ventana.quit)

        # Entradas para los números
        self.entry_ancho = tk.Entry(self.ventana)
        self.entry_ancho.pack(pady=5)
        self.entry_ancho.insert(0, "Ancho")

        self.entry_alto = tk.Entry(self.ventana)
        self.entry_alto.pack(pady=5)
        self.entry_alto.insert(0, "Alto")

        self.ventana.mainloop()

    def cambiar_tamano(self):
        ancho = int(self.entry_ancho.get())
        alto = int(self.entry_alto.get())
        self.ventana.geometry(f"{ancho}x{alto}")


Aplicacion()
