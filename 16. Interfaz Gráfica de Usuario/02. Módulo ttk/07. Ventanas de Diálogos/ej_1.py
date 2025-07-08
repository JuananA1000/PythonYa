'''
  Confeccionar una aplicación que muestre un diálogo cuando se seleccione una opción de un menú.
  El dialogo debe solicitar el ingreso de dos enteros que se utilizarán en la ventana principal para redimensionarla.
'''

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.agregar_menu()
        self.ventana.mainloop()

    def agregar_menu(self):
        self.barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.barra_menu)
        self.opciones = tk.Menu(self.barra_menu, tearoff=0)
        self.opciones.add_command(label="Configurar Ventana", command=self.configurar)
        self.barra_menu.add_cascade(label="Opciones", menu=self.opciones)

    def configurar(self):
        dialogo = DialogoTamaño(self.ventana)
        s = dialogo.mostrar()
        self.ventana.geometry(f"{s[0]}x{s[1]}")

class DialogoTamaño:
    def __init__(self, ventanaprincipal):
        self.dialogo = tk.Toplevel(ventanaprincipal)

        self.label1 = ttk.Label(self.dialogo, text="Ancho:")
        self.label1.grid(row=0, column=0, padx=5, pady=5)

        self.dato1 = tk.StringVar()

        self.entry1 = ttk.Entry(self.dialogo, textvariable=self.dato1)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        self.entry1.focus()  # Para que el cursor esté en este campo al abrir el diálogo

        self.label2 = ttk.Label(self.dialogo, text="Alto:")
        self.label2.grid(row=1, column=0, padx=5, pady=5)

        self.dato2 = tk.StringVar()

        self.entry2 = ttk.Entry(self.dialogo, textvariable=self.dato2)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        self.boton_aceptar = ttk.Button(self.dialogo, text="Aceptar", command=self.confirmar)
        self.boton_aceptar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.dialogo.protocol("WM_DELETE_WINDOW", self.confirmar)  # Para cerrar el diálogo con la X
        self.dialogo.resizable(0, 0)
        self.dialogo.grab_set()  # Para que el diálogo sea modal

    def mostrar(self):
        self.dialogo.wait_window()  # Espera a que se cierre el diálogo

        return (self.dato1.get(), self.dato2.get())

    def confirmar(self):
        self.dialogo.destroy()


Aplicacion()
