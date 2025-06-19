'''
  Disponer dos objetos de la clase Button con las etiquetas: "varón" y "mujer", al presionarse mostrar en la barra de 
  títulos de la ventana la etiqueta del botón presionado. 
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sexo")

        self.boton_varon = tk.Button(self.ventana, text="H", command=self.mostrar_varon)
        self.boton_varon.pack(side=tk.LEFT, padx=10, pady=10)

        self.boton_mujer = tk.Button(self.ventana, text="M", command=self.mostrar_mujer)
        self.boton_mujer.pack(side=tk.LEFT, padx=10, pady=10)

        self.ventana.mainloop()

    def mostrar_varon(self):
        self.ventana.title("V")

    def mostrar_mujer(self):
        self.ventana.title("M")


Aplicacion()
