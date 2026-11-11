'''
  Por defecto no aparece una barra de scroll si la cantidad de item supera el tamaño del cuadro del Listbox. Para que se
  muestre una barra de scroll la debemos crear y enlazar con el Listbox.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.listbox = tk.Listbox(self.ventana, width=30, height=10)
        self.listbox.grid(row=0, column=0)

        self.scroll = tk.Scrollbar(self.ventana, orient=tk.VERTICAL, command=self.listbox.yview)  # Orientación vertical
        self.scroll.grid(row=0, column=1, sticky="NS")  # NS para que ocupe todo el alto

        for i in range(50):
            self.listbox.insert(tk.END, f"Elemento {i + 1}")

        self.boton = tk.Button(self.ventana, text="Seleccionar", command=self.seleccionar)
        self.boton.grid(row=1, column=0)

        self.label = tk.Label(self.ventana, text="Selecciona un elemento")
        self.label.grid(row=2, column=0)

        self.ventana.mainloop()

    def seleccionar(self):
        seleccion = self.listbox.curselection()

        if seleccion:
            indice = seleccion[0]
            valor = self.listbox.get(indice)
            self.label.config(text=f"Elemento seleccionado: {valor}")


Aplicacion()
