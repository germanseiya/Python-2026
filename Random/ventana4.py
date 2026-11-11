import wx
import os

class MiAplicacion(wx.Frame):
    def __init__(self):
        super().__init__(
            None,
            title="Mi Aplicación wxPython",
            size=(500, 600)
        )

        panel = wx.Panel(self)

        # Carpeta donde está guardado este archivo Python
        carpeta = os.path.dirname(os.path.abspath(__file__))

        # Cargar imagen
        img_path = os.path.join(carpeta, "Miku.jpg")

        if os.path.exists(img_path):
            image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)

            if image.IsOk():
                image = image.Scale(
                    1920, 1080,
                    wx.IMAGE_QUALITY_HIGH
                )

                self.bitmap = wx.Bitmap(image)
                self.img_ctrl = wx.StaticBitmap(
                    panel,
                    bitmap=self.bitmap,
                    pos=(0, 0)
                )
        else:
            wx.MessageBox(
                f"No se encontró la imagen:\n{img_path}",
                "Error de imagen",
                wx.OK | wx.ICON_ERROR
            )

        # Botón
        self.btn = wx.Button(
            panel,
            label="¡Presiona Espacio!",
            pos=(150, 480),
            size=(200, 40)
        )

        # Audio
        self.audio_path = os.path.join(
            carpeta,
            "Warmness On The Soul.wav"
        )

        self.sound = None

        if os.path.exists(self.audio_path):
            try:
                self.sound = wx.Sound(self.audio_path)
            except Exception as e:
                print("Error al cargar audio:", e)

        # Evento de teclado
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_down)

        self.Centre()
        self.Show()

    def on_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_SPACE:
            if self.sound and self.sound.IsOk():
                self.sound.Play(wx.SOUND_ASYNC)

        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    MiAplicacion()
    app.MainLoop()