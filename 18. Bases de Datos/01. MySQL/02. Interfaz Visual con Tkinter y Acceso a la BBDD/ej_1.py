'''
  Desarrollar una aplicación visual con la librería tkinter que permita implementar los algoritmos de carga de 
  artículos, consulta por código y listado completo.
  Seguiremos trabajando con la tabla 'articulos' que creamos en el concepto anterior.
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos


class Aplicacion:
    def __init__(self):
        self.articulo = articulos.Articulos()

        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio 1")

        self.cuaderno = ttk.Notebook(self.ventana)
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()

        self.cuaderno.grid(row=0, column=0, padx=10, pady=10)

        self.ventana.mainloop()

    def carga_articulos(self):
        self.pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina, text="Carga de Artículos")

        self.labelframe = ttk.LabelFrame(self.pagina, text="Artículo")
        self.labelframe.grid(row=0, column=0, padx=10, pady=10)

        self.label1 = ttk.Label(self.labelframe, text="Descripción: ")
        self.label1.grid(row=0, column=0, padx=4, pady=4)
        self.descripcioncarga = tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(row=0, column=1, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe, text="Precio: ")
        self.label2.grid(row=1, column=0, padx=4, pady=4)
        self.preciocarga = tk.StringVar()
        self.entryprecio = ttk.Entry(self.labelframe, textvariable=self.preciocarga)
        self.entryprecio.grid(row=1, column=1, padx=4, pady=4)

        self.boton = ttk.Button(self.labelframe, text="Cargar", command=self.agregar)
        self.boton.grid(row=2, column=0, columnspan=2, padx=4, pady=4)

    def agregar(self):
        descripcion = (self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo.alta(descripcion)
        mb.showinfo("Información", "Artículo cargado correctamente")

        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        self.pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina, text="Consulta por Código")

        self.labelframe = ttk.LabelFrame(self.pagina, text="Artículo")
        self.labelframe.grid(row=0, column=0, padx=10, pady=10)

        self.label1 = ttk.Label(self.labelframe, text="Código: ")
        self.label1.grid(row=0, column=0, padx=4, pady=4)
        self.codigoconsulta = tk.StringVar()
        self.entrycodigo = ttk.Entry(self.labelframe, textvariable=self.codigoconsulta)
        self.entrycodigo.grid(row=0, column=1, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe, text="Descripción: ")
        self.label2.grid(row=1, column=0, padx=4, pady=4)
        self.descripcionconsulta = tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe, textvariable=self.descripcionconsulta, state="readonly")
        self.entrydescripcion.grid(row=1, column=1, padx=4, pady=4)

        self.label3 = ttk.Label(self.labelframe, text="Precio: ")
        self.label3.grid(row=2, column=0, padx=4, pady=4)
        self.precioconsulta = tk.StringVar()
        self.entryprecio = ttk.Entry(self.labelframe, textvariable=self.precioconsulta, state="readonly")
        self.entryprecio.grid(row=2, column=1, padx=4, pady=4)

        self.boton = ttk.Button(self.labelframe, text="Consultar", command=self.consultar)
        self.boton.grid(row=3, column=0, columnspan=2, padx=4, pady=4)

    def consultar(self):
        codigo = (self.codigoconsulta.get(),)
        resultado = self.articulo.consulta(codigo)

        if resultado:
            self.descripcionconsulta.set(resultado[0][1])
            self.precioconsulta.set(resultado[0][2])
        else:
            mb.showinfo("Información", "No se encontró el artículo")
            self.descripcionconsulta.set("")
            self.precioconsulta.set("")

    def listado_completo(self):
        self.pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina, text="Listado Completo")

        self.labelframe = ttk.LabelFrame(self.pagina, text="Artículos")
        self.labelframe.grid(row=0, column=0, padx=10, pady=10)

        self.boton = ttk.Button(self.labelframe, text="Listar", command=self.listar)
        self.boton.grid(row=0, column=0, padx=4, pady=4)

        self.texto = st.ScrolledText(self.labelframe, width=40, height=10)
        self.texto.grid(row=1, column=0, padx=4, pady=4)

    def listar(self):
        resultado = self.articulo.listado()
        self.texto.delete(1.0, tk.END)

        for articulo in resultado:
            self.texto.insert(tk.END, f"Código: {articulo[0]}, Descripción: {articulo[1]}, Precio: {articulo[2]}\n")


Aplicacion()
