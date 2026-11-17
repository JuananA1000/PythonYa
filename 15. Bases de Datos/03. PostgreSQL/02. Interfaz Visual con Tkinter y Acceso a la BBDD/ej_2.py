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
        self.articulo1 = articulos.Articulos()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")

        self.cuaderno1 = ttk.Notebook(self.ventana1)

        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrar_articulo()
        self.modificar_articulo()

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)

        self.ventana1.mainloop()

    # ---------------------------------
    # CARGA DE ARTÍCULOS
    # ---------------------------------

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")

        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Artículo")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.descripcioncarga = tk.StringVar()
        self.entrydescripcion = ttk.Entry(
            self.labelframe1,
            textvariable=self.descripcioncarga
        )
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Precio:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.preciocarga = tk.StringVar()
        self.entryprecio = ttk.Entry(
            self.labelframe1,
            textvariable=self.preciocarga
        )
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        self.boton1 = ttk.Button(
            self.labelframe1,
            text="Confirmar",
            command=self.agregar
        )
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos = (
            self.descripcioncarga.get(),
            self.preciocarga.get()
        )

        self.articulo1.alta(datos)

        mb.showinfo("Información", "Los datos fueron cargados")

        self.descripcioncarga.set("")
        self.preciocarga.set("")

    # ---------------------------------
    # CONSULTA POR CÓDIGO
    # ---------------------------------

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")

        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label3 = ttk.Label(self.labelframe2, text="Código:")
        self.label3.grid(column=0, row=0, padx=4, pady=4)

        self.codigo = tk.StringVar()
        self.entrycodigo = ttk.Entry(
            self.labelframe2,
            textvariable=self.codigo
        )
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label4 = ttk.Label(self.labelframe2, text="Descripción:")
        self.label4.grid(column=0, row=1, padx=4, pady=4)

        self.descripcion = tk.StringVar()
        self.entrydescripcion = ttk.Entry(
            self.labelframe2,
            textvariable=self.descripcion,
            state="readonly"
        )
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

        self.label5 = ttk.Label(self.labelframe2, text="Precio:")
        self.label5.grid(column=0, row=2, padx=4, pady=4)

        self.precio = tk.StringVar()
        self.entryprecio = ttk.Entry(
            self.labelframe2,
            textvariable=self.precio,
            state="readonly"
        )
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        self.boton2 = ttk.Button(
            self.labelframe2,
            text="Consultar",
            command=self.consultar
        )
        self.boton2.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(),)

        respuesta = self.articulo1.consulta(datos)

        if len(respuesta) > 0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set("")
            self.precio.set("")

            mb.showinfo(
                "Información",
                "No existe un artículo con dicho código"
            )

    # ---------------------------------
    # LISTADO COMPLETO
    # ---------------------------------

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        self.boton3 = ttk.Button(
            self.labelframe3,
            text="Listado completo",
            command=self.listar
        )
        self.boton3.grid(column=0, row=0, padx=4, pady=4)

        self.scrolledtext1 = st.ScrolledText(
            self.labelframe3,
            width=30,
            height=10
        )
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta = self.articulo1.recuperar_todos()

        self.scrolledtext1.delete("1.0", tk.END)

        for fila in respuesta:
            self.scrolledtext1.insert(
                tk.END,
                "código:" + str(fila[0]) +
                "\ndescripción:" + fila[1] +
                "\nprecio:" + str(fila[2]) + "\n\n"
            )

    # ---------------------------------
    # BORRAR ARTÍCULO
    # ---------------------------------

    def borrar_articulo(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrar artículo")

        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Artículo")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        self.label6 = ttk.Label(self.labelframe4, text="Código:")
        self.label6.grid(column=0, row=0, padx=4, pady=4)

        self.codigoborrar = tk.StringVar()
        self.entrycodigoborrar = ttk.Entry(
            self.labelframe4,
            textvariable=self.codigoborrar
        )
        self.entrycodigoborrar.grid(column=1, row=0, padx=4, pady=4)

        self.boton4 = ttk.Button(
            self.labelframe4,
            text="Borrar",
            command=self.borrar
        )
        self.boton4.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos = (self.codigoborrar.get(),)

        respuesta = self.articulo1.consulta(datos)

        if len(respuesta) > 0:
            self.articulo1.borrar(datos)

            mb.showinfo(
                "Información",
                "Artículo eliminado correctamente"
            )

            self.codigoborrar.set("")
        else:
            mb.showinfo(
                "Información",
                "No existe un artículo con dicho código"
            )

    # ---------------------------------
    # MODIFICAR ARTÍCULO
    # ---------------------------------

    def modificar_articulo(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar artículo")

        self.labelframe5 = ttk.LabelFrame(self.pagina5, text="Artículo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        self.label7 = ttk.Label(self.labelframe5, text="Código:")
        self.label7.grid(column=0, row=0, padx=4, pady=4)

        self.codigomodificar = tk.StringVar()
        self.entrycodigomodificar = ttk.Entry(
            self.labelframe5,
            textvariable=self.codigomodificar
        )
        self.entrycodigomodificar.grid(column=1, row=0, padx=4, pady=4)

        self.label8 = ttk.Label(self.labelframe5, text="Descripción:")
        self.label8.grid(column=0, row=1, padx=4, pady=4)

        self.descripcionmodificar = tk.StringVar()
        self.entrydescripcionmodificar = ttk.Entry(
            self.labelframe5,
            textvariable=self.descripcionmodificar
        )
        self.entrydescripcionmodificar.grid(column=1, row=1, padx=4, pady=4)

        self.label9 = ttk.Label(self.labelframe5, text="Precio:")
        self.label9.grid(column=0, row=2, padx=4, pady=4)

        self.preciomodificar = tk.StringVar()
        self.entrypreciomodificar = ttk.Entry(
            self.labelframe5,
            textvariable=self.preciomodificar
        )
        self.entrypreciomodificar.grid(column=1, row=2, padx=4, pady=4)

        self.boton5 = ttk.Button(
            self.labelframe5,
            text="Consultar",
            command=self.consultar_modificar
        )
        self.boton5.grid(column=1, row=3, padx=4, pady=4)

        self.boton6 = ttk.Button(
            self.labelframe5,
            text="Modificar",
            command=self.modificar
        )
        self.boton6.grid(column=1, row=4, padx=4, pady=4)

    def consultar_modificar(self):
        datos = (self.codigomodificar.get(),)

        respuesta = self.articulo1.consulta(datos)

        if len(respuesta) > 0:
            self.descripcionmodificar.set(respuesta[0][0])
            self.preciomodificar.set(respuesta[0][1])
        else:
            self.descripcionmodificar.set("")
            self.preciomodificar.set("")

            mb.showinfo(
                "Información",
                "No existe un artículo con dicho código"
            )

    def modificar(self):
        datos = (
            self.descripcionmodificar.get(),
            self.preciomodificar.get(),
            self.codigomodificar.get()
        )

        respuesta = self.articulo1.consulta(
            (self.codigomodificar.get(),)
        )

        if len(respuesta) > 0:
            self.articulo1.modificar(datos)

            mb.showinfo(
                "Información",
                "Artículo modificado correctamente"
            )

            self.codigomodificar.set("")
            self.descripcionmodificar.set("")
            self.preciomodificar.set("")
        else:
            mb.showinfo(
                "Información",
                "No existe un artículo con dicho código"
            )


Aplicacion()
