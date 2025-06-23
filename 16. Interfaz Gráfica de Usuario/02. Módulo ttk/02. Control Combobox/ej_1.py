'''
  Mostrar en una ventana un control de tipo Combobox con los días de la semana. Cuando se presione un botón actualizar 
  una Label con el día seleccionado.
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Selector de Días de la Semana")

        self.label_title = tk.Label(self.ventana, text="Seleccione un día de la semana:")
        self.label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        self.combobox = ttk.Combobox(self.ventana, values=self.dias_semana)
        self.combobox.grid(row=1, column=0, padx=10, pady=10)

        self.boton_actualizar = tk.Button(self.ventana, text="Actualizar Día", command=self.actualizar_dia)
        self.boton_actualizar.grid(row=1, column=1, padx=10, pady=10)

        self.label_resultado = tk.Label(self.ventana, text="")
        self.label_resultado.grid(row=2, column=0, columnspan=2)

        self.ventana.mainloop()

    def actualizar_dia(self):
        dia_seleccionado = self.combobox.get()
        self.label_resultado.config(text=f"Día seleccionado: {dia_seleccionado}")


Aplicacion()
