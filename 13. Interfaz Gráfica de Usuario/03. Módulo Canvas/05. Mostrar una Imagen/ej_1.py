'''
  Se cuenta con tres archivos de tipo png con las imágenes de distintas cartas. Mostrarlas a cada una dentro de una 
  componente de tipo Canvas.
'''

import tkinter as tk
from pathlib import Path  # Con esta librería obtenemos la ruta del archivo actual y nos curamos en salud


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Mostrar Imagenes")
        self.canvas = tk.Canvas(self.ventana, width=700, height=400, background="black")
        self.canvas.grid(row=0, column=0)

        img1 = tk.PhotoImage(file=Path(__file__).parent / "carta1.png")
        self.canvas.create_image(30, 50, anchor=tk.NW, image=img1)

        img2 = tk.PhotoImage(file=Path(__file__).parent / "carta2.png")
        self.canvas.create_image(240, 50, anchor=tk.NW, image=img2)

        img3 = tk.PhotoImage(file=Path(__file__).parent / "carta3.png")
        self.canvas.create_image(450, 50, anchor=tk.NW, image=img3)

        self.ventana.mainloop()


Aplicacion()
