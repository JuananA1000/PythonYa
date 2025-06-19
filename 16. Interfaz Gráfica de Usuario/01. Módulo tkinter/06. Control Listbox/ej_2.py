'''
  Disponer un Listbox con una serie de nombres de frutas. Permitir la selección de varias frutas. Cuando se presione un 
  botón recuperar todas las frutas seleccionadas y mostrarlas en una Label.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.listbox = tk.Listbox(self.ventana, selectmode=tk.MULTIPLE)
        self.listbox.grid(column=0, row=0)

        for fruta in ["Manzana", "Banana", "Naranja", "Pera", "Uva"]:
            self.listbox.insert(tk.END, fruta)

        self.boton = tk.Button(self.ventana, text="Seleccionar", command=self.recuperar)
        self.boton.grid(column=0, row=1)

        self.label = tk.Label(self.ventana, text="")
        self.label.grid(column=0, row=2)

        self.ventana.mainloop()

    def recuperar(self):
        frutas_seleccionadas = [self.listbox.get(i) for i in self.listbox.curselection()]
        self.label.config(text=f"Frutas seleccionadas: {', '.join(frutas_seleccionadas)}")


Aplicacion()
