'''
  Mostrar una ventana con un botón en su interior. Al ser presionado mostrar un mensaje.
'''

import wx


class Ventana(wx.Frame):

    # *args es una lista de argumentos que se pasan a la clase que se está llamando
    # **kw es un diccionario de argumentos que se pasan a la clase que se está llamando
    def __init__(self, *args, **kw):
        super(Ventana, self).__init__(*args, **kw)
        self.boton = wx.Button(self, label="Click aquí")
        self.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        wx.MessageBox("Hola Mundo")


app = wx.App()
ventana = Ventana(None)
ventana.Show()
app.MainLoop()
