'''
  Ingresar el nombre de usuario y clave en controles de tipo Entry. Si se ingresa las cadena (usuario: juan, 
  clave="abc123") luego mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje 
  "Incorrecto". Utilizar Widget del módulo ttk.
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Validador de usuario")

        self.label_user = ttk.Label(self.ventana, text="Usuario:")
        self.label_user.grid(row=0, column=0)
        self.user = tk.StringVar()
        self.entry_user = ttk.Entry(self.ventana, width=30, textvariable=self.user)
        self.entry_user.grid(row=0, column=1)

        self.label_passw = ttk.Label(self.ventana, text="Contraseña:")
        self.label_passw.grid(row=1, column=0)
        self.passw = tk.StringVar()
        self.entry_passw = ttk.Entry(self.ventana, width=30, textvariable=self.passw, show="*")
        self.entry_passw.grid(row=1, column=1)

        self.boton = ttk.Button(self.ventana, text="Validar", command=self.validar_pass)
        self.boton.grid(row=2, column=0, columnspan=2)

        self.ventana.mainloop()

    def validar_pass(self):
        user = self.user.get()
        passw = self.passw.get()

        if user == "juan" and passw == "abc123":
            self.ventana.title("Correcto")
        else:
            self.ventana.title("Incorrecto")


Aplicacion()
