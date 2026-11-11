import wx

# Inicializar la aplicación
app = wx.App()

# Crear la ventana principal (Frame)
ventana = wx.Frame(None, title="Hola wxPython", size=(400, 350))
panel = wx.Panel(ventana)

# Añadir un texto estático
texto = wx.StaticText(panel, label="¡Interfaz nativa lista!", pos=(20, 20))

# --- Cargar y mostrar la imagen de forma directa ---
# Cargamos la imagen directamente como Bitmap para evitar errores de escala
bitmap = wx.Bitmap('Miku.jpg', wx.BITMAP_TYPE_ANY)

# Creamos el control estático para mostrarla en pantalla
imagen_control = wx.StaticBitmap(panel, bitmap=bitmap, pos=(20, 60))

# Mostrar ventana y ejecutar el bucle de eventos
ventana.Show()
app.MainLoop()