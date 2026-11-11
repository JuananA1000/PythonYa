'''
  Mostrar dos controles de tipo Radiobutton con las etiquetas "Varón" y "Mujer", cuando se presione un botón actualizar 
  una Label con el Radiobutton seleccionado.
'''
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label = tk.Label(self.ventana, text="Selecciona una opción:")
        self.label.grid(row=0, column=2, padx=10, pady=10)

        self.seleccion = tk.IntVar()
        self.seleccion.set(2)

        self.radiobutton_varon = tk.Radiobutton(self.ventana, text="Varón", variable=self.seleccion, value=1)
        self.radiobutton_varon.grid(row=0, column=0, padx=10, pady=10)

        self.radiobutton_mujer = tk.Radiobutton(self.ventana, text="Mujer", variable=self.seleccion, value=2)
        self.radiobutton_mujer.grid(row=0, column=1, padx=10, pady=10)

        self.boton_actualizar = tk.Button(self.ventana, text="Actualizar", command=self.actualizar_label)
        self.boton_actualizar.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.ventana.mainloop()

    def actualizar_label(self):
        if self.seleccion.get() == 1:
            texto = "Has seleccionado Varón"
        else:
            texto = "Has seleccionado Mujer"

        self.label.config(text=texto)


Aplicacion()
