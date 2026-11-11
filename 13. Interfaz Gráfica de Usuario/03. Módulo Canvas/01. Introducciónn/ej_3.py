'''
  Crear una aplicación que solicite el ingreso de tres valores por teclado que representan las cantidades de votos 
  obtenidas por tres partidos políticos. Luego mostrar un gráfico de tartas.
'''

import tkinter as tk
from tkinter import ttk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Elecciones 2026")

        self.entrada_datos()

        self.canvas = tk.Canvas(self.ventana, width=600, height=400, background="white")
        self.canvas.grid(row=1, column=0)

        self.ventana.mainloop()

    def entrada_datos(self):
        self.lf = ttk.LabelFrame(self.ventana, text="Ingrese los votos de cada partido")
        self.lf.grid(row=0, column=0, sticky="w")

        self.label1 = ttk.Label(self.lf, text="Partido A:")
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        self.votos_a = tk.IntVar()
        self.entry1 = ttk.Entry(self.lf, textvariable=self.votos_a)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.label2 = ttk.Label(self.lf, text="Partido B:")
        self.label2.grid(row=1, column=0, padx=5, pady=5)
        self.votos_b = tk.IntVar()
        self.entry2 = ttk.Entry(self.lf, textvariable=self.votos_b)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        self.label3 = ttk.Label(self.lf, text="Partido C:")
        self.label3.grid(row=2, column=0, padx=5, pady=5)
        self.votos_c = tk.IntVar()
        self.entry3 = ttk.Entry(self.lf, textvariable=self.votos_c)
        self.entry3.grid(row=2, column=1, padx=5, pady=5)

        self.label4 = ttk.Label(self.lf, text="Partido D:")
        self.label4.grid(row=3, column=0, padx=5, pady=5)
        self.votos_d = tk.IntVar()
        self.entry4 = ttk.Entry(self.lf, textvariable=self.votos_d)
        self.entry4.grid(row=3, column=1, padx=5, pady=5)

        self.boton = ttk.Button(self.lf, text="Mostrar Gráfico", command=self.grafico_tarta)
        self.boton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def grafico_tarta(self):
        # self.canvas.delete(tk.ALL) # borrar el contenido del Canvas:
        valor1 = int(self.votos_a.get())
        valor2 = int(self.votos_b.get())
        valor3 = int(self.votos_c.get())
        valor4 = int(self.votos_d.get())

        suma = valor1 + valor2 + valor3 + valor4

        grados1 = (valor1 / suma) * 360
        grados2 = (valor2 / suma) * 360
        grados3 = (valor3 / suma) * 360
        grados4 = (valor4 / suma) * 360

        self.canvas.create_arc(10, 10, 400, 400, fill="red", start=0, extent=grados1)
        self.canvas.create_arc(10, 10, 400, 400, fill="blue", start=grados1, extent=grados2)
        self.canvas.create_arc(10, 10, 400, 400, fill="green", start=grados1+grados2, extent=grados3)
        self.canvas.create_arc(10, 10, 400, 400, fill="purple", start=grados1+grados2+grados3, extent=grados4)
        self.canvas.create_text(205, 50, text="partido A", fill="white", font="Arial")
        self.canvas.create_text(205, 160, text="partido B", fill="white", font="Arial")
        self.canvas.create_text(205, 270, text="partido C", fill="white", font="Arial")
        self.canvas.create_text(205, 380, text="partido D", fill="white", font="Arial")


Aplicacion()
