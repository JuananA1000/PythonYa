'''
  Confeccionar un programa que permita ingresar dos números en controles de tipo Entry, luego sumar los dos valores 
  ingresados y mostrar la suma en una Label al presionar un botón. 
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Suma")

        self.label1 = tk.Label(self.ventana, text="Nº1:")
        self.label1.grid(row=0, column=0)
        self.numero1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana, width=30, textvariable=self.numero1)
        self.entry1.grid(row=0, column=1)

        self.label2 = tk.Label(self.ventana, text="Nº1:")
        self.label2.grid(row=1, column=0)
        self.numero2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana, width=30, textvariable=self.numero2)
        self.entry2.grid(row=1, column=1)

        self.boton = tk.Button(self.ventana, text="Sumar", command=self.sumar)
        self.boton.grid(row=2, column=0, columnspan=2)

        self.resultado = tk.StringVar()
        self.label_resultado = tk.Label(self.ventana, textvariable=self.resultado)
        self.label_resultado.grid(row=3, column=0, columnspan=2)

        self.ventana.mainloop()

    def sumar(self):
        num1 = int(self.numero1.get())
        num2 = int(self.numero2.get())

        suma = num1 + num2

        self.resultado.set(f"Total: {suma}")


Aplicacion()
