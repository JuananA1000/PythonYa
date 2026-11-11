'''
  Confeccionar un programa que cree un objeto de la clase Canvas y muestre la funcionalidad de las principales 
  figuras planas.
'''

import tkinter as tk

class Aplicacion:
  def __init__(self):
    self.ventana = tk.Tk()
    self.ventana.title("Figuras planas")

    self.canvas = tk.Canvas(self.ventana, width=400, height=400, background="black")
    self.canvas.grid(row=0, column=0)

    # Dibujar figuras planas
    self.canvas.create_line(0, 0, 100, 50, fill="white") # Línea
    self.canvas.create_rectangle(150, 50, 250, 150, fill="blue") # Rectángulo
    self.canvas.create_oval(50, 200, 150, 400, fill="red") # Óvalo, pero se pueden hacer círculos si se ajustan las coordenadas
    self.canvas.create_polygon(200, 200, 250, 250, 300, 200, fill="green") # Polígono
    self.canvas.create_arc(50, 50, 150, 150, start=0, extent=180, fill="yellow") # Arco relleno
    
    self.ventana.mainloop()

Aplicacion()