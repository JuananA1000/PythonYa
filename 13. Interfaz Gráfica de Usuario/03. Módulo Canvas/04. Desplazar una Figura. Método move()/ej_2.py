'''
  Modificar el problema que desplaza un cuadrado con las teclas de flechas de tal modo que la figura no pueda salir del 
  espacio definido para el Canvas.
  Para saber la posición actual de una figura la clase Canvas cuenta con el método 'coords':

  x1, y1, x2, y2 = self.canvas1.coords(self.cuadrado)
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
        '''
        Código repetitivo
        '''
        # if evento.keysym == 'Right' and self.canvas.coords(self.cuadrado)[2] < 300:
        #     self.canvas.move(self.cuadrado, 4, 0)
        # elif evento.keysym == 'Left' and self.canvas.coords(self.cuadrado)[0] > 0:
        #     self.canvas.move(self.cuadrado, -4, 0)
        # elif evento.keysym == 'Up' and self.canvas.coords(self.cuadrado)[1] > 0:
        #     self.canvas.move(self.cuadrado, 0, -4)
        # elif evento.keysym == 'Down' and self.canvas.coords(self.cuadrado)[3] < 200:
        #     self.canvas.move(self.cuadrado, 0, 4)

        '''
        Código optimizado
        '''
        x1, y1, x2, y2 = self.canvas.coords(self.cuadrado)

        movimientos = {
            'Right': (4, 0, x2 < 300),
            'Left': (-4, 0, x1 > 0),
            'Up': (0, -4, y1 > 0),
            'Down': (0, 4, y2 < 200)
        }

        if evento.keysym in movimientos:
            dx, dy, dentro_limites = movimientos[evento.keysym]

            if dentro_limites:
                self.canvas.move(self.cuadrado, dx, dy)


Aplicacion()
