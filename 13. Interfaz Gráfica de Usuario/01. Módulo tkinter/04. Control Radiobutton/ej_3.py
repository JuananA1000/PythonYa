'''
  Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'. Cuando se presione un botón 
  cambiar el color de fondo del formulario.
  Si consideramos que la variable ventana1 es un objeto de la clase Tk, luego si queremos que el fondo sea de color rojo 
  debemos llamar al método configure y en el parámetro bg indicar un string con el color a activar ("red", "green" o 
  "blue"):
  
  self.ventana1.configure(bg="red")
'''

import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.seleccion = tk.StringVar()
        self.seleccion.set("rojo")  # Valor por defecto
        
        self.radiobutton_r = tk.Radiobutton(self.ventana, text="Rojo", variable=self.seleccion, value="rojo")
        self.radiobutton_r.grid(row=2, column=0, padx=10, pady=10)

        self.radiobutton_v = tk.Radiobutton(self.ventana, text="Verde", variable=self.seleccion, value="verde")
        self.radiobutton_v.grid(row=2, column=1, padx=10, pady=10)

        self.radiobutton_a = tk.Radiobutton(self.ventana, text="Azul", variable=self.seleccion, value="azul")
        self.radiobutton_a.grid(row=2, column=2, padx=10, pady=10)

        self.boton_set_color = tk.Button(self.ventana, text="Set Color", command=self.set_color)
        self.boton_set_color.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.ventana.mainloop()

    def set_color(self):
     
        if self.seleccion.get() == "rojo":
            self.ventana.configure(bg="red")
        elif self.seleccion.get() == "verde":
            self.ventana.configure(bg="green")
        elif self.seleccion.get() == "azul":
            self.ventana.configure(bg="blue")


Aplicacion()
