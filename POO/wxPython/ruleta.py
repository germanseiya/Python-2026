import wx
import wx.media
import os
import winsound
import random

class MiAplicacion(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Mi Aplicación con Probabilidades", size=(500, 650))
        
        panel = wx.Panel(self)
        carpeta = os.path.dirname(os.path.abspath(__file__))
        
        # --- SISTEMA DE PROBABILIDADES ---
        # Generamos un número del 1 al 100
        suerte = random.randint(1, 100)
        print(f"Número de probabilidad generado: {suerte}")

        # 1. 1% de probabilidad: Aparece un video (ejemplo desde URL directa)
        if suerte == 1:
            print("¡Evento Raro! 1%: Reproduciendo video.")
            try:
                self.media_ctrl = wx.media.MediaCtrl(panel, szBackend=wx.media.MEDIABACKEND_WMP10, pos=(50, 50), size=(400, 300))
                # Puedes cambiar esta URL por un enlace directo a un archivo .mp4 en la web
                self.media_ctrl.Load("https://youtu.be/dQw4w9WgXcQ?si=nD3wlauXfgxZLaU6")
                self.media_ctrl.Play()
            except Exception as e:
                print("Error al cargar el video:", e)

        # 2. 10% de probabilidad (del 2 al 11): Aparece una imagen especial de Miku
        elif 2 <= suerte <= 11:
            print("¡Evento Poco Común! 10%: Miku especial.")
            img_path = os.path.join(carpeta, "Miku.jpg") # O una variante especial si tienes otra
            if os.path.exists(img_path):
                image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
                image = image.Scale(300, 300, wx.IMAGE_QUALITY_HIGH)
                self.bitmap = wx.Bitmap(image)
                self.img_ctrl = wx.StaticBitmap(panel, bitmap=self.bitmap, pos=(100, 100))

        # 3. 89% de probabilidad restante: Comportamiento normal (tu imagen por defecto)
        else:
            print("¡Evento Normal! 89%: Reproduciendo video.")
            try:
                self.media_ctrl = wx.media.MediaCtrl(panel, szBackend=wx.media.MEDIABACKEND_WMP10, pos=(50, 50), size=(400, 300))
                # Puedes cambiar esta URL por un enlace directo a un archivo .mp4 en la web
                self.media_ctrl.Load("https://youtu.be/cu9EYHjohp0?si=RRuFjgRraBW8-PMd")
                self.media_ctrl.Play()
            except Exception as e:
                print("Error al cargar el video:", e)

        # --- BOTÓN Y AUDIO ---
        self.btn = wx.Button(panel, label="¡Presiona Espacio!", pos=(150, 520), size=(200, 40))
        
        # Ruta del archivo de audio .wav
        self.audio_path = os.path.join(carpeta, "Warmness On The Soul.wav")

        # Vincular evento de teclado para reproducir audio con la barra espaciadora
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_down)

        self.Centre()
        self.Show()

        def on_key_down(self, event):
                if event.GetKeyCode() == wx.WXK_SPACE:
                    if os.path.exists(self.audio_path):
                        winsound.PlaySound(self.audio_path, winsound.SND_ASYNC | winsound.SND_FILENAME)
                event.Skip()

if __name__ == '__main__':
    app = wx.App()
    MiAplicacion()
    app.MainLoop()