'''
  Crear una ventana con un Canvas de 600 × 400 píxeles y fondo negro que permita:
  - Mostrar las coordenadas del ratón en el título de la ventana.
  - Dibujar un pequeño círculo rojo al hacer clic con el botón izquierdo.
'''

import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("600x400")

        self.canvas = tk.Canvas(self.ventana, width=600, height=400, bg="black")
        self.canvas.pack()

        self.canvas.bind("<Motion>", self.mostrar_coordenadas)
        self.canvas.bind("<Button-1>", self.dibujar_circulo)

        self.ventana.mainloop()

    def mostrar_coordenadas(self, evento):
        self.ventana.title(f"Captura de eventos del mouse - Coordenadas: ({evento.x}, {evento.y})")

    def dibujar_circulo(self, evento):
        radio = 3
        self.canvas.create_oval(evento.x-radio, evento.y-radio, evento.x+radio, evento.y+radio, fill="grey", outline="red")


Aplicacion()
