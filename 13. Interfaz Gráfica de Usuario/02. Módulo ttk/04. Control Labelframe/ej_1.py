'''
  Confeccionar una aplicación que muestre dos controles de tipo LabelFrame. En la primera disponer 2 Label, 2 Entry y un 
  Button, en el segundo LabelFrame disponer 3 botones.
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.lf_login = ttk.LabelFrame(self.ventana, text="Login:")
        self.lf_login.grid(column=0, row=0, padx=5, pady=10)

        self.login()

        self.lf_operaciones = ttk.LabelFrame(self.ventana, text="Operaciones")
        self.lf_operaciones.grid(column=0, row=1, padx=5, pady=10)

        self.operaciones()

        self.ventana.mainloop()

    def login(self):
        self.label_user = ttk.Label(self.lf_login, text="Nombre de usuario:")
        self.label_user.grid(column=0, row=0, padx=4, pady=4)

        self.entry_user = ttk.Entry(self.lf_login)
        self.entry_user.grid(column=1, row=0, padx=4, pady=4)

        self.label_pass = ttk.Label(self.lf_login, text="Ingrese clave:")
        self.label_pass.grid(column=0, row=1, padx=4, pady=4)

        self.entry_pass = ttk.Entry(self.lf_login, show="*")
        self.entry_pass.grid(column=1, row=1, padx=4, pady=4)

        self.btn_login = ttk.Button(self.lf_login, text="Ingresar")
        self.btn_login.grid(column=1, row=2, padx=4, pady=4)

    def operaciones(self):
        self.btn_agregar = ttk.Button(self.lf_operaciones, text="Agregar usuario")
        self.btn_agregar.grid(column=0, row=0, padx=4, pady=4)

        self.btn_modificar = ttk.Button(self.lf_operaciones, text="Modificar usuario")
        self.btn_modificar.grid(column=1, row=0, padx=4, pady=4)

        self.btn_borrar = ttk.Button(self.lf_operaciones, text="Borrar usuario")
        self.btn_borrar.grid(column=2, row=0, padx=4, pady=4)


Aplicacion()
