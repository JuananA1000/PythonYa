'''
  Mostrar los botones del 1 al 5. Cuando se presiona mostrar en una Label todos los botones presionados hasta ese 
  momento.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Botones")

        self.botones = []
        self.pulsados = []

        for i in range(1, 6):
            # command=lambda i=i: self.pulsar_boton(i) crea una función anónima que captura el valor actual de i para cada botón.
            boton = tk.Button(self.ventana, text=str(i), command=lambda i=i: self.pulsar_boton(i))
            boton.pack(side=tk.LEFT, padx=10, pady=10)
            self.botones.append(boton)

        self.label_pulsados = tk.Label(self.ventana, text="Botones pulsados:")
        self.label_pulsados.pack(padx=10, pady=10)  # los padx y pady alinean los botonesl

        self.ventana.mainloop()

    def pulsar_boton(self, numero):
        self.pulsados.append(str(numero))
        self.label_pulsados.config(text="Botones pulsados: " + ", ".join(self.pulsados))


Aplicacion()
