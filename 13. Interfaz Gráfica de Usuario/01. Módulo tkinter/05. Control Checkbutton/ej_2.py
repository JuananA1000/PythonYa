'''
  Disponer un control Checkbutton que muestre el siguiente mensaje: ¿Está de acuerdo con los términos y condiciones?, 
  además agregar un Button desactivo. Cuando se tilde el Checkbutton inmediatamente activar el botón.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.check_var = tk.IntVar()
        self.checkbutton = tk.Checkbutton(self.ventana, text="¿Está de acuerdo con los términos y condiciones?", variable=self.check_var, command=self.activar_boton)
        self.checkbutton.pack(padx=10, pady=10)

        self.boton = tk.Button(self.ventana, text="Aceptar", state=tk.DISABLED)
        self.boton.pack(padx=10, pady=10)

        self.ventana.mainloop()

    def activar_boton(self):
        if self.check_var.get() == 1:
            self.boton.config(state=tk.NORMAL)
        else:
            self.boton.config(state=tk.DISABLED)

Aplicacion()
