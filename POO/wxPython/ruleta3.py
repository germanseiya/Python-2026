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
        # (Lo dejamos en 1 para forzar el video y probar)
        suerte = 1  # Luego puedes cambiarlo por random.randint(1, 100)
        print(f"Número de probabilidad generado: {suerte}")

        # 1. 1% de probabilidad: Carga el video local (Rickrol.mp4)
        if suerte == 1:
            print("¡Evento Raro! 1%: Reproduciendo video.")
            try:
                self.media_ctrl = wx.media.MediaCtrl(panel, pos=(0, 0), size=(1920, 1080))
                
                # Nombre de tu archivo de video
                video_path = os.path.join(carpeta, "Rickrol.mp4")
                
                if os.path.exists(video_path):
                    self.media_ctrl.Load(video_path)
                    self.media_ctrl.Play()
                else:
                    print("Aviso: No se encontró el archivo 'Rickrol.mp4'.")
            except Exception as e:
                print("Error al cargar el video:", e)

        # 2. 10% de probabilidad (del 2 al 11): Miku especial
        elif 2 <= suerte <= 11:
            print("¡Evento Poco Común! 10%: Miku especial.")
            img_path = os.path.join(carpeta, "Miku.jpg")
            if os.path.exists(img_path):
                image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
                image = image.Scale(300, 300, wx.IMAGE_QUALITY_HIGH)
                self.bitmap = wx.Bitmap(image)
                self.img_ctrl = wx.StaticBitmap(panel, bitmap=self.bitmap, pos=(100, 100))

        # 3. 89% restante: Imagen normal
        else:
            print("¡Evento Normal! 89%: Imagen por defecto.")
            img_path = os.path.join(carpeta, "Miku.jpg")
            if os.path.exists(img_path):
                image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
                image = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
                self.bitmap = wx.Bitmap(image)
                self.img_ctrl = wx.StaticBitmap(panel, bitmap=self.bitmap, pos=(150, 150))

        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    MiAplicacion()
    app.MainLoop()