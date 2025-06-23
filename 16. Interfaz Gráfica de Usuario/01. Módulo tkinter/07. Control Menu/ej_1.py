'''
  Confeccionar una aplicación que muestre dos opciones en el menú de barra superior. La primer opción despliega un
  submenú que permita cambiar el color de fondo del formulario y la segunda permita cambiar el tamaño de formulario
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejemplo de Menú")

        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)

        # Submenú para el color de fondo
        opcion_color = tk.Menu(barra_menu)
        opcion_color.add_command(label="Rojo", command=self.fijar_rojo)
        opcion_color.add_command(label="Verde", command=self.fijar_verde)
        opcion_color.add_separator()  # Agrega una línea separadora (opcional)
        opcion_color.add_command(label="Azul", command=self.fijar_azul)
        barra_menu.add_cascade(label="Colores", menu=opcion_color)  # Agregamos un desplegable al menú principal

        #  Controles de teclado para cambiar el color de fondo
        self.ventana.bind_all("<Control-r>", self.cambiar)
        self.ventana.bind_all("<Control-g>", self.cambiar)
        self.ventana.bind_all("<Control-b>", self.cambiar)

        # Submenú para el tamaño de la ventana
        opcion_tamano = tk.Menu(barra_menu)
        opcion_tamano.add_command(label="640x480", command=self.ventana_s)
        opcion_tamano.add_command(label="1024x800", command=self.ventana_l)
        barra_menu.add_cascade(label="Tamano", menu=opcion_tamano)

        self.ventana.mainloop()

    def cambiar(self, event):
        if event.keysym == 'r':
            self.fijar_rojo()
        elif event.keysym == 'g':
            self.fijar_verde()
        elif event.keysym == 'b':
            self.fijar_azul()

    def fijar_rojo(self):
        self.ventana.config(bg='red')

    def fijar_verde(self):
        self.ventana.config(bg='green')

    def fijar_azul(self):
        self.ventana.config(bg='blue')

    def ventana_s(self):
        self.ventana.geometry("640x480")

    def ventana_l(self):
        self.ventana.geometry("1024x800")


Aplicacion()
