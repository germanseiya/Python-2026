import wx
import os

class MiAplicacion(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Mi Aplicación wxPython", size=(500, 600))
        
        panel = wx.Panel(self)
        
        # 1. Imagen de fondo (asegúrate de que miku.png esté en la carpeta)
        try:
            img_path = "Miku.jpg"
            image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
            # Escalamos la imagen para que se ajuste a la ventana de forma proporcional
            image = image.Scale(500, 500, wx.IMAGE_QUALITY_HIGH)
            self.bitmap = wx.Bitmap(image)
            self.img_ctrl = wx.StaticBitmap(panel, bitmap=self.bitmap, pos=(0, 0))
        except Exception as e:
            print("No se pudo cargar la imagen:", e)

        # 2. Botón (equivalente al Button de Kivy)
        self.btn = wx.Button(panel, label="¡Presiona Espacio!", pos=(150, 480), size=(200, 40))
        # En wxPython la opacidad total no se maneja igual en todos los sistemas operativos mediante el botón directo, 
        # pero podemos ocultarlo o mostrarlo si lo deseas. Aquí lo dejamos visible.
        
        # 3. Cargar audio (equivalente a SoundLoader de Kivy)
        self.audio_path = "Warmness On The Soul.wav"
        self.sound = None
        if os.path.exists(self.audio_path):
            # wx.Sound soporta archivos WAV principalmente en la mayoría de plataformas. 
            # Si es MP3 y da problemas, se recomienda usar formato WAV.
            try:
                self.sound = wx.Sound(self.audio_path)
            except:
                pass

        # Vincular evento de teclado (equivalente a Window.bind en Kivy)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_down)

        self.Centre()
        self.Show()

    def on_key_down(self, event):
        # Detectar si se presionó la barra espaciadora (código ASCII o Keycode para espacio es WXK_SPACE)
        code = event.GetKeyCode()
        if code == wx.WXK_SPACE:
            if self.sound and self.sound.IsOk():
                # Reproducir sonido de forma asíncrona
                self.sound.Play(wx.SOUND_ASYNC)
        
        # Continuar propagando el evento
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    MiAplicacion()
    app.MainLoop()