'''
  Mostrar una ventana y en su interior tres controles de tipo Checkbutton cuyas etiquetas correspondan a distintos 
  lenguajes de programación. Cuando se presione un botón mostrar en una Label la cantidad de Checkbutton que se 
  encuentran chequeados.
'''
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Contador de Checkbuttons")

        self.check_var1 = tk.IntVar()
        self.check_var2 = tk.IntVar()
        self.check_var3 = tk.IntVar()

        self.checkbutton1 = tk.Checkbutton(self.ventana, text="Python", variable=self.check_var1)
        self.checkbutton1.grid(row=0, column=0, padx=10, pady=10)

        self.checkbutton2 = tk.Checkbutton(self.ventana, text="Java", variable=self.check_var2)
        self.checkbutton2.grid(row=0, column=1, padx=10, pady=10)

        self.checkbutton3 = tk.Checkbutton(self.ventana, text="JavaScript", variable=self.check_var3)
        self.checkbutton3.grid(row=0, column=2, padx=10, pady=10)

        self.boton_contar = tk.Button(self.ventana, text="Contar Seleccionados", command=self.contar_checkbuttons)
        self.boton_contar.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.label_resultado = tk.Label(self.ventana, text="")
        self.label_resultado.grid(row=2, column=0, columnspan=3)

        self.ventana.mainloop()

    def contar_checkbuttons(self):
        contador = 0

        if self.check_var1.get() == 1:
            contador += 1
        if self.check_var2.get() == 1:
            contador += 1
        if self.check_var3.get() == 1:
            contador += 1

        self.label_resultado.config(text=f"Checkbuttons seleccionados: {contador}")

Aplicacion()
