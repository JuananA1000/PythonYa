'''
  Agregar dos pestañas al programa de administración de artículos que permitan borrar un artículo ingresando su código y 
  otra opción que permita consultar y modificar la descripción y precio de un artículo.
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
        self.ventana.title("Ejercicio 2")

        self.cuaderno = ttk.Notebook(self.ventana)

        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrar_articulo()
        self.modif_articulo()

        self.cuaderno.grid(row=0, column=0, padx=10, pady=10)

        self.ventana.mainloop()

    # ---------------------------------
    # PESTAÑA 1: CARGA DE ARTÍCULOS
    # ---------------------------------

    def carga_articulos(self):
        self.pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina, text="Carga de Artículos")

        self.labelframe = ttk.LabelFrame(self.pagina, text="Artículo")
        self.labelframe.grid(row=0, column=0, padx=10, pady=10)

        self.label1 = ttk.Label(self.labelframe, text="Descripción: ")
        self.label1.grid(row=0, column=0, padx=4, pady=4)

        self.descripcioncarga = tk.StringVar()
        self.entrydescripcion = ttk.Entry(
            self.labelframe,
            textvariable=self.descripcioncarga
        )
        self.entrydescripcion.grid(row=0, column=1, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe, text="Precio: ")
        self.label2.grid(row=1, column=0, padx=4, pady=4)

        self.preciocarga = tk.StringVar()
        self.entryprecio = ttk.Entry(
            self.labelframe,
            textvariable=self.preciocarga
        )
        self.entryprecio.grid(row=1, column=1, padx=4, pady=4)

        self.boton = ttk.Button(
            self.labelframe,
            text="Cargar",
            command=self.agregar
        )
        self.boton.grid(row=2, column=0, columnspan=2, padx=4, pady=4)

    def agregar(self):
        descripcion = (
            self.descripcioncarga.get(),
            self.preciocarga.get()
        )

        self.articulo.alta(descripcion)

        mb.showinfo("Información", "Artículo cargado correctamente")

        self.descripcioncarga.set("")
        self.preciocarga.set("")

    # ---------------------------------
    # PESTAÑA 2: CONSULTA POR CÓDIGO
    # ---------------------------------

    def consulta_por_codigo(self):
        self.pagina_consulta = ttk.Frame(self.cuaderno)
        self.cuaderno.add(
            self.pagina_consulta,
            text="Consulta por Código"
        )

        self.labelframe_consulta = ttk.LabelFrame(
            self.pagina_consulta,
            text="Artículo"
        )
        self.labelframe_consulta.grid(row=0, column=0, padx=10, pady=10)

        self.label1 = ttk.Label(
            self.labelframe_consulta,
            text="Código: "
        )
        self.label1.grid(row=0, column=0, padx=4, pady=4)

        self.codigoconsulta = tk.StringVar()
        self.entrycodigo_consulta = ttk.Entry(
            self.labelframe_consulta,
            textvariable=self.codigoconsulta
        )
        self.entrycodigo_consulta.grid(row=0, column=1, padx=4, pady=4)

        self.label2 = ttk.Label(
            self.labelframe_consulta,
            text="Descripción: "
        )
        self.label2.grid(row=1, column=0, padx=4, pady=4)

        self.descripcionconsulta = tk.StringVar()
        self.entrydescripcion_consulta = ttk.Entry(
            self.labelframe_consulta,
            textvariable=self.descripcionconsulta,
            state="readonly"
        )
        self.entrydescripcion_consulta.grid(
            row=1, column=1, padx=4, pady=4
        )

        self.label3 = ttk.Label(
            self.labelframe_consulta,
            text="Precio: "
        )
        self.label3.grid(row=2, column=0, padx=4, pady=4)

        self.precioconsulta = tk.StringVar()
        self.entryprecio_consulta = ttk.Entry(
            self.labelframe_consulta,
            textvariable=self.precioconsulta,
            state="readonly"
        )
        self.entryprecio_consulta.grid(
            row=2, column=1, padx=4, pady=4
        )

        self.boton_consultar = ttk.Button(
            self.labelframe_consulta,
            text="Consultar",
            command=self.consultar
        )
        self.boton_consultar.grid(
            row=3, column=0, columnspan=2, padx=4, pady=4
        )

    def consultar(self):
        codigo = (self.codigoconsulta.get(),)

        resultado = self.articulo.consulta(codigo)

        if resultado:
            self.descripcionconsulta.set(resultado[0][0])
            self.precioconsulta.set(resultado[0][1])
        else:
            mb.showinfo("Información", "No se encontró el artículo")
            self.descripcionconsulta.set("")
            self.precioconsulta.set("")

    # ---------------------------------
    # PESTAÑA 3: LISTADO COMPLETO
    # ---------------------------------

    def listado_completo(self):
        self.pagina_listado = ttk.Frame(self.cuaderno)
        self.cuaderno.add(
            self.pagina_listado,
            text="Listado Completo"
        )

        self.labelframe_listado = ttk.LabelFrame(
            self.pagina_listado,
            text="Artículos"
        )
        self.labelframe_listado.grid(row=0, column=0, padx=10, pady=10)

        self.boton_listar = ttk.Button(
            self.labelframe_listado,
            text="Listar",
            command=self.listar
        )
        self.boton_listar.grid(row=0, column=0, padx=4, pady=4)

        self.texto = st.ScrolledText(
            self.labelframe_listado,
            width=40,
            height=10
        )
        self.texto.grid(row=1, column=0, padx=4, pady=4)

    def listar(self):
        resultado = self.articulo.recuperar_todos()

        self.texto.delete(1.0, tk.END)

        for articulo in resultado:
            self.texto.insert(
                tk.END,
                f"Código: {articulo[0]}, "
                f"Descripción: {articulo[1]}, "
                f"Precio: {articulo[2]}\n"
            )

    # ---------------------------------
    # PESTAÑA 4: BORRAR ARTÍCULO
    # ---------------------------------

    def borrar_articulo(self):
        self.pagina_borrar = ttk.Frame(self.cuaderno)
        self.cuaderno.add(
            self.pagina_borrar,
            text="Borrar Artículo"
        )

        self.labelframe_borrar = ttk.LabelFrame(
            self.pagina_borrar,
            text="Artículo"
        )
        self.labelframe_borrar.grid(row=0, column=0, padx=10, pady=10)

        self.label1 = ttk.Label(
            self.labelframe_borrar,
            text="Código: "
        )
        self.label1.grid(row=0, column=0, padx=4, pady=4)

        self.codigoborrar = tk.StringVar()
        self.entrycodigo_borrar = ttk.Entry(
            self.labelframe_borrar,
            textvariable=self.codigoborrar
        )
        self.entrycodigo_borrar.grid(row=0, column=1, padx=4, pady=4)

        self.boton_borrar = ttk.Button(
            self.labelframe_borrar,
            text="Borrar",
            command=self.borrar
        )
        self.boton_borrar.grid(
            row=1, column=0, columnspan=2, padx=4, pady=4
        )

    def borrar(self):
        codigo = (self.codigoborrar.get(),)

        resultado = self.articulo.consulta(codigo)

        if resultado:
            self.articulo.baja(codigo)

            mb.showinfo(
                "Información",
                "Artículo borrado correctamente"
            )

            self.codigoborrar.set("")
        else:
            mb.showinfo("Información", "No se encontró el artículo")

    # ---------------------------------
    # PESTAÑA 5: MODIFICAR ARTÍCULO
    # ---------------------------------

    def modif_articulo(self):
        self.pagina_modificar = ttk.Frame(self.cuaderno)
        self.cuaderno.add(
            self.pagina_modificar,
            text="Modificar Artículo"
        )

        self.labelframe_modificar = ttk.LabelFrame(
            self.pagina_modificar,
            text="Artículo"
        )
        self.labelframe_modificar.grid(row=0, column=0, padx=10, pady=10)

        self.label1 = ttk.Label(
            self.labelframe_modificar,
            text="Código: "
        )
        self.label1.grid(row=0, column=0, padx=4, pady=4)

        self.codigomodificar = tk.StringVar()
        self.entrycodigo_modificar = ttk.Entry(
            self.labelframe_modificar,
            textvariable=self.codigomodificar
        )
        self.entrycodigo_modificar.grid(row=0, column=1, padx=4, pady=4)

        self.label2 = ttk.Label(
            self.labelframe_modificar,
            text="Descripción: "
        )
        self.label2.grid(row=1, column=0, padx=4, pady=4)

        self.descripcionmodificar = tk.StringVar()
        self.entrydescripcion_modificar = ttk.Entry(
            self.labelframe_modificar,
            textvariable=self.descripcionmodificar
        )
        self.entrydescripcion_modificar.grid(
            row=1, column=1, padx=4, pady=4
        )

        self.label3 = ttk.Label(
            self.labelframe_modificar,
            text="Precio: "
        )
        self.label3.grid(row=2, column=0, padx=4, pady=4)

        self.preciomodificar = tk.StringVar()
        self.entryprecio_modificar = ttk.Entry(
            self.labelframe_modificar,
            textvariable=self.preciomodificar
        )
        self.entryprecio_modificar.grid(
            row=2, column=1, padx=4, pady=4
        )

        self.boton_modificar = ttk.Button(
            self.labelframe_modificar,
            text="Modificar",
            command=self.modificar
        )
        self.boton_modificar.grid(
            row=3, column=0, columnspan=2, padx=4, pady=4
        )

    def modificar(self):
        codigo = (self.codigomodificar.get(),)

        resultado = self.articulo.consulta(codigo)

        if resultado:
            descripcion = self.descripcionmodificar.get()
            precio = self.preciomodificar.get()

            datos = (descripcion, precio, codigo[0])

            self.articulo.actualizar(datos)

            mb.showinfo(
                "Información",
                "Artículo modificado correctamente"
            )
        else:
            mb.showinfo("Información", "No se encontró el artículo")


Aplicacion()