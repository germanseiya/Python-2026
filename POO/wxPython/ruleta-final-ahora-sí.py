import wx
import wx.media
import os
import random

class MiAplicacion(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Ruleta de Miku y Videos", size=(800, 600))
        
        panel = wx.Panel(self)
        carpeta = os.path.dirname(os.path.abspath(__file__))
        
        suerte = random.randint(1, 100)
        print(f"Número de probabilidad generado: {suerte}")

        pantalla_ancho, pantalla_alto = wx.GetDisplaySize()

        if suerte == 10:
            print("¡¡Reproduciendo Video 1!")
            self.cargar_video(panel, carpeta, "Rickrol.wmv", pantalla_ancho, pantalla_alto)

        elif 2 <= suerte <= 10:
            print("¡Reproduciendo Video 2!")
            self.cargar_video(panel, carpeta, "Katyusha.wmv", pantalla_ancho, pantalla_alto)
        
        elif 3 <= suerte <= 10:
            print("¡Reproduciendo Video 3!")
            self.cargar_video(panel, carpeta, "erika.wmv", pantalla_ancho, pantalla_alto)

        elif 4 <= suerte <= 10:
            print("¡Reproduciendo Video 4!")
            self.cargar_video(panel, carpeta, "al.wmv", pantalla_ancho, pantalla_alto)

        elif 5 <= suerte <= 10:
            print("¡Reproduciendo Video 5!")
            self.cargar_video(panel, carpeta, "mundian.wmv", pantalla_ancho, pantalla_alto)
        else:
            print("Imagen normal por defecto.")
            self.mostrar_imagen(panel, carpeta, "miku.png", pantalla_ancho, pantalla_alto)

        self.ShowFullScreen(True)
        self.Centre()
        self.Show()

    def cargar_video(self, panel, carpeta, nombre_video, ancho, alto):
        """Función para inicializar y cargar videos en pantalla completa"""
        try:
            self.media_ctrl = wx.media.MediaCtrl(
                panel,
                size=(ancho, alto),
                szBackend=wx.media.MEDIABACKEND_WMP10
            )
        except Exception:
            self.media_ctrl = wx.media.MediaCtrl(panel, size=(ancho, alto))

        self.media_ctrl.Bind(wx.media.EVT_MEDIA_LOADED, self.on_media_loaded)
        
        video_path = os.path.join(carpeta, nombre_video)
        if os.path.exists(video_path):
            self.media_ctrl.Load(video_path)
            print(f"Cargando video: {nombre_video}")
        else:
            print(f"Aviso: No se encontró el archivo '{nombre_video}'.")

    def on_media_loaded(self, event):
        """Se ejecuta cuando el video termina de cargarse y se reproduce"""
        self.media_ctrl.Play()

    def mostrar_imagen(self, panel, carpeta, nombre_archivo, ancho, alto):
        """Función auxiliar para mostrar una imagen adaptada a pantalla completa"""
        img_path = os.path.join(carpeta, nombre_archivo)
        if os.path.exists(img_path):
            image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
            image = image.Scale(ancho, alto, wx.IMAGE_QUALITY_HIGH)
            self.bitmap = wx.Bitmap(image)
            self.img_ctrl = wx.StaticBitmap(panel, bitmap=self.bitmap, pos=(0, 0))

if __name__ == '__main__':
    app = wx.App()
    MiAplicacion()
    app.MainLoop()