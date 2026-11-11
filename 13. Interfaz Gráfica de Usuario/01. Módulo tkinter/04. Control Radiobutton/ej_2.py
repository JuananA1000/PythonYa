'''
  Disponer dos controles de tipo Entry para el ingreso de enteros. Mediante dos controles Radiobutton permitir 
  seleccionar si queremos sumarlos o restarlos. Al presionar un botón mostrar el resultado de la operación seleccionada.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label_num1 = tk.Label(self.ventana, text="Número 1:")
        self.label_num1.grid(row=0, column=0, padx=10, pady=10)
        self.entry_num1 = tk.Entry(self.ventana)
        self.entry_num1.grid(row=0, column=1, padx=10, pady=10)

        self.label_num2 = tk.Label(self.ventana, text="Número 2:")
        self.label_num2.grid(row=1, column=0, padx=10, pady=10)
        self.entry_num2 = tk.Entry(self.ventana)
        self.entry_num2.grid(row=1, column=1, padx=10, pady=10)

        self.seleccion = tk.StringVar()
        self.seleccion.set("sumar")

        self.radiobutton_sumar = tk.Radiobutton(self.ventana, text="Sumar", variable=self.seleccion, value="sumar")
        self.radiobutton_sumar.grid(row=2, column=0, padx=10, pady=10)

        self.radiobutton_restar = tk.Radiobutton(self.ventana, text="Restar", variable=self.seleccion, value="restar")
        self.radiobutton_restar.grid(row=2, column=1, padx=10, pady=10)

        self.boton_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular_resultado)
        self.boton_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.resultado_label = tk.Label(self.ventana, text="")
        self.resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.ventana.mainloop()

    def calcular_resultado(self):
        num1 = int(self.entry_num1.get())
        num2 = int(self.entry_num2.get())
        resultado = 0

        if self.seleccion.get() == "sumar":
            resultado = num1 + num2
        else:
            resultado = num1 - num2

        self.resultado_label.config(text=f"Resultado: {resultado}")


Aplicacion()
