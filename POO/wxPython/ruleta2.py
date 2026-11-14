import wx
import wx.media
import os
import random

class MiAplicacion(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Mi Aplicación con Probabilidades", size=(500, 650))
        
        panel = wx.Panel(self)
        carpeta = os.path.dirname(os.path.abspath(__file__))
        
        # --- SISTEMA DE PROBABILIDADES ---
        suerte = random.randint(1, 100)
        print(f"Número de probabilidad generado: {suerte}")

        # 1. 1% de probabilidad: Aparece un video 
        # (Usa un archivo local con os.path.join o un enlace directo .mp4 de internet)
        if suerte == 50:
            print("¡Evento Raro! 50%: Reproduciendo video.")
            try:
                self.media_ctrl = wx.media.MediaCtrl(panel, szBackend=wx.media.MEDIABACKEND_WMP10, pos=(0, 0), size=(1920, 1080))
                # Ejemplo con enlace directo de video .mp4 válido:
                self.media_ctrl.Load(os.path.join(carpeta, "Rickrol.mp4"))
                self.media_ctrl.Play()
            except Exception as e:
                print("Error al cargar el video:", e)

        # 2. 10% de probabilidad (del 2 al 11): Miku especial
        elif 2 <= suerte <= 40:
            print("¡Evento Raro! 45%: Reproduciendo video.")
            try:
                self.media_ctrl = wx.media.MediaCtrl(panel, szBackend=wx.media.MEDIABACKEND_WMP10, pos=(0, 0), size=(1920, 1080))
                # Ejemplo con enlace directo de video .mp4 válido:
                self.media_ctrl.Load(os.path.join(carpeta, "Katyusha.mp4"))
                self.media_ctrl.Play()
            except Exception as e:
                print("Error al cargar el video:", e)
        # 3. 89% de probabilidad restante: Muestra la imagen normal por defecto
        else:
            print("¡Evento Normal! 10%: Imagen por defecto.")
            img_path = os.path.join(carpeta, "Miku.jpg")
            if os.path.exists(img_path):
                image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
                image = image.Scale(1920, 1080, wx.IMAGE_QUALITY_HIGH)
                self.bitmap = wx.Bitmap(image)
                self.img_ctrl = wx.StaticBitmap(panel, bitmap=self.bitmap, pos=(0, 0))

        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    MiAplicacion()
    app.MainLoop()