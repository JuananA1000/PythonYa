'''
  Disponer un botón y mostrar al azar una de las tres cartas del problema anterior. Cada vez que se presione el botón 
  generar un valor aleatorio y a partir de dicho valor mostrar una carta.
'''

import tkinter as tk
import random
from pathlib import Path  # Con esta librería obtenemos la ruta del archivo actual y nos curamos en salud


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Mostrar Imagenes")
        self.canvas = tk.Canvas(self.ventana, width=700, height=400, background="black")
        self.canvas.grid(row=0, column=0)

        self.boton = tk.Button(self.ventana, text="Mostrar Carta", command=self.mostrar_carta_random)
        self.boton.grid(row=1, column=0)

        self.ventana.mainloop()

    def mostrar_carta_random(self):
        carta = random.choice(["carta1.png", "carta2.png", "carta3.png"])
        img = tk.PhotoImage(file=Path(__file__).parent / carta)
        self.canvas.create_image(30, 50, anchor=tk.NW, image=img)
        self.canvas.image = img  # Guardar referencia a la imagen para que no se elimine


Aplicacion()
