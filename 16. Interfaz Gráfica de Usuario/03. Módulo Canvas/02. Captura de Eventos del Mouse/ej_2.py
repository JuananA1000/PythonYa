'''
  Crear un Canvas de 600 × 400 píxeles con fondo negro que permita dibujar trazos rojos arrastrando el ratón mientras se 
  mantiene pulsado el botón izquierdo
'''

import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("600x400")
        self.ventana.title("Captura de eventos del mouse")

        self.canvas = tk.Canvas(self.ventana, width=600, height=400, bg="black")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.dibujar_trazo)

        self.ventana.mainloop()

    def dibujar_trazo(self, evento):
        radio = 3
        self.canvas.create_oval(evento.x-radio, evento.y-radio, evento.x+radio,
                                evento.y+radio, fill="red", outline="red")


Aplicacion()
