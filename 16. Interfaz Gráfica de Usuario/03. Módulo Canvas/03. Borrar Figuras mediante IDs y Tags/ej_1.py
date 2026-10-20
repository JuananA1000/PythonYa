'''
  Confeccionar un programa que cree un objeto de la clase Canvas y luego dibuje:
  - una línea
  - un réctángulo
  - un óvalo

  Almacenar el id de cada dibujo en un atributo.
  Crear también 3 cuadrados y definir el parámetro tag con el mismo valor para cada uno de ellos.
  Mediante cinco botones permitir borrar: 
  - la línea
  - el rectángulo
  - el óvalo
  - todos los cuadrados
  - todas las figuras contenidas en el objeto Canvas.
'''

import tkinter as tk
from tkinter import ttk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Borrar figuras mediante IDs y tags")

        self.crear_botones()

        self.canvas = tk.Canvas(self.ventana, width=300, height=300)
        self.canvas.grid(row=1, column=0)

        self.linea = self.canvas.create_line(10, 10, 200, 200)
        self.rectangulo = self.canvas.create_rectangle(50, 50, 150, 150)
        self.ovalo = self.canvas.create_oval(100, 100, 200, 200)
        self.canvas.create_rectangle(20, 20, 40, 40, tag="cuadrado")
        self.canvas.create_rectangle(60, 60, 80, 80, tag="cuadrado")
        self.canvas.create_rectangle(100, 100, 120, 120, tag="cuadrado")

        self.ventana.mainloop()

    def crear_botones(self):
        self.labelframe = ttk.LabelFrame(self.ventana, text="Borrar figuras")
        self.labelframe.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.btn1 = ttk.Button(self.labelframe, text="Borrar línea", command=self.borrar_linea)
        self.btn1.grid(column=0, row=0, padx=5)

        self.btn2 = ttk.Button(self.labelframe, text="Borrar rectángulo", command=self.borrar_rectangulo)
        self.btn2.grid(column=1, row=0, padx=5)

        self.btn3 = ttk.Button(self.labelframe, text="Borrar óvalo", command=self.borrar_ovalo)
        self.btn3.grid(column=2, row=0, padx=5)

        self.btn4 = ttk.Button(self.labelframe, text="Borrar cuadrados", command=self.borrar_cuadrados)
        self.btn4.grid(column=3, row=0, padx=5)

        self.btn5 = ttk.Button(self.labelframe, text="Borrar todo", command=self.borrar_todo)
        self.btn5.grid(column=4, row=0, padx=5)

    def borrar_linea(self):
        self.canvas.delete(self.linea)

    def borrar_rectangulo(self):
        self.canvas.delete(self.rectangulo)

    def borrar_cuadrados(self):
        self.canvas.delete("cuadrado")

    def borrar_ovalo(self):
        self.canvas.delete(self.ovalo)

    def borrar_todo(self):
        self.canvas.delete(tk.ALL)


Aplicacion()
