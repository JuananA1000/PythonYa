'''
  Confeccionar un programa que que muestre un cuadrado dentro de un Canvas. Cuando se presione alguna de las teclas de 
  flecha proceder a desplazar la figura 4 píxeles teniendo en cuenta la dirección de la tecla de flecha presionada.
'''

import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.canvas = tk.Canvas(self.ventana, width=300, height=200, background="black")
        self.canvas.grid(row=0, column=0)
        self.cuadrado = self.canvas.create_rectangle(150, 10, 200, 60, fill="red")

        self.ventana.bind("<KeyPress>", self.pulsar_tecla)
        self.ventana.mainloop()

    def pulsar_tecla(self, evento):
        if evento.keysym == 'Right':
            self.canvas.move(self.cuadrado, 4, 0)
        elif evento.keysym == 'Left':
            self.canvas.move(self.cuadrado, -4, 0)
        elif evento.keysym == 'Up':
            self.canvas.move(self.cuadrado, 0, -4)
        elif evento.keysym == 'Down':
            self.canvas.move(self.cuadrado, 0, 4)


Aplicacion()
