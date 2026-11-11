'''
  Mostrar una ventana y en su interior dos botones y una label. La label muestra inicialmente el valor 1. Cada uno de 
  los botones permiten incrementar o decrementar en uno el contenido de la label.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor = 1

        self.ventana = tk.Tk()
        self.ventana.title("Controles Button y Label")

        self.label = tk.Label(self.ventana, text=self.valor)
        self.label.grid(row=0, column=0)
        self.label.configure(foreground="red")

        self.boton_mas = tk.Button(self.ventana, text="+", command=self.incrementar)
        self.boton_mas.grid(row=0, column=1)

        self.boton_menos = tk.Button(self.ventana, text="-", command=self.decrementar)
        self.boton_menos.grid(row=0, column=2)

        # Este método se encarga de mantener la ventana abierta y procesar eventos hasta que el usuario la cierre.
        self.ventana.mainloop()

    def incrementar(self):
        self.valor += 1
        self.label.configure(text=self.valor)

    def decrementar(self):
        self.valor -= 1
        self.label.configure(text=self.valor)


Aplicacion()
