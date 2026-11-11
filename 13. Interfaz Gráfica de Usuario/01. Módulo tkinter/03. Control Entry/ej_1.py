'''
  Confeccionar una aplicación que permita ingresar un entero por teclado y al presionar un botón muestre dicho valor 
  elevado al cuadrado en una Label.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label1 = tk.Label(self.ventana, text="Ingresa un número:")
        self.label1.grid(row=0, column=0)

        self.dato = tk.StringVar()

        self.entry = tk.Entry(self.ventana, width=10, textvariable=self.dato)
        self.entry.grid(row=1, column=0)

        self.boton = tk.Button(self.ventana, text="Calcular cuadrado", command=self.calcular_cuadrado)
        self.boton.grid(row=2, column=0)

        self.label2 = tk.Label(self.ventana, text="Resultado:")
        self.label2.grid(row=3, column=0)

        self.ventana.mainloop()

    def calcular_cuadrado(self):
        numero = int(self.dato.get())
        resultado = numero ** 2
        self.label2.config(text=f" {numero}² = {resultado}")


Aplicacion()
