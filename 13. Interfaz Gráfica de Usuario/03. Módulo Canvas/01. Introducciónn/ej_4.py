'''
  Implementar un gráfico estadístico de tipo "Barra Porcentual".
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

        self.boton = ttk.Button(self.lf, text="Mostrar Gráfico", command=self.grafico_barra_porcent)
        self.boton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def grafico_barra_porcent(self):
        # self.canvas.delete(tk.ALL)

        valor1 = int(self.votos_a.get())
        valor2 = int(self.votos_b.get())
        valor3 = int(self.votos_c.get())
        valor4 = int(self.votos_d.get())

        suma = valor1 + valor2 + valor3 + valor4
        ancho_total = 400

        ancho1 = ancho_total * valor1 / suma
        ancho2 = ancho_total * valor2 / suma
        ancho3 = ancho_total * valor3 / suma
        ancho4 = ancho_total * valor4 / suma

        x = 10
        self.canvas.create_rectangle(x, 50, x + ancho1, 100, fill="blue")
        x += ancho1
        self.canvas.create_rectangle(x, 50, x + ancho2, 100, fill="red")
        x += ancho2
        self.canvas.create_rectangle(x, 50, x + ancho3, 100, fill="green")
        x += ancho3
        self.canvas.create_rectangle(x, 50, x + ancho4, 100, fill="purple")


Aplicacion()
