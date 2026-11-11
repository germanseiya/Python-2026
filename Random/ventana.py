import wx

# Inicializar la aplicación
app = wx.App()

# Crear la ventana principal (Frame)
ventana = wx.Frame(None, title="Hola wxPython", size=(350, 200))
panel = wx.Panel(ventana)

# Añadir un texto estático
texto = wx.StaticText(panel, label="¡Interfaz nativa lista!", pos=(20, 20))

# Mostrar ventana y ejecutar el bucle de eventos
ventana.Show()
app.MainLoop()