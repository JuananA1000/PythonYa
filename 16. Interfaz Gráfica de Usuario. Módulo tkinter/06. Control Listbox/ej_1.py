'''
  Disponer un Listbox con una serie de nombres de frutas. Permitir la selección solo de uno de ellos. Cuando se presione 
  un botón recuperar la fruta seleccionada y mostrarla en una Label.
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        # Por defecto, el selectmode es SINGLE, veremos la selección MULTIPLE en el siguiente ejercicio
        self.listbox = tk.Listbox(self.ventana)
        self.listbox.grid(column=0, row=0)

        for fruta in ["Manzana", "Banana", "Naranja", "Pera", "Uva"]:
            self.listbox.insert(tk.END, fruta)

        self.boton = tk.Button(self.ventana, text="Seleccionar", command=self.recuperar)
        self.boton.grid(column=0, row=1)

        self.label = tk.Label(self.ventana, text="")
        self.label.grid(column=0, row=2)

        self.ventana.mainloop()

    def recuperar(self):
        fruta_seleccionada = self.listbox.get(tk.ACTIVE)
        self.label.config(text=f"Fruta seleccionada: {fruta_seleccionada}")


Aplicacion()
