import wx
import os
import winsound  # <-- Importamos el módulo nativo de Windows para audio

class MiAplicacion(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Mi Aplicación wxPython", size=(500, 600))
        
        panel = wx.Panel(self)
        
        # Carpeta donde está guardado este archivo Python
        carpeta = os.path.dirname(os.path.abspath(__file__))
        
        # Cargar imagen (manteniendo tu código que ya funciona)
        img_path = os.path.join(carpeta, "Miku.jpg")
        if os.path.exists(img_path):
            image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
            image = image.Scale(1920, 1080, wx.IMAGE_QUALITY_HIGH)
            self.bitmap = wx.Bitmap(image)
            self.img_ctrl = wx.StaticBitmap(panel, bitmap=self.bitmap, pos=(0, 0))

        # Ruta del archivo de audio .wav
        self.audio_path = os.path.join(carpeta, "Warmness On The Soul.wav")

        # Evento de teclado
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_down)

        self.Centre()
        self.Show()

    def on_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_SPACE:
            if os.path.exists(self.audio_path):
                # Reproduce el audio de forma asíncrona (SND_ASYNC) para que no se pegue la ventana
                winsound.PlaySound(self.audio_path, winsound.SND_ASYNC | winsound.SND_FILENAME)
        
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    MiAplicacion()
    app.MainLoop()