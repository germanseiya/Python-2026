import wx
import wx.media
import os

class MiAplicacion(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Mi Aplicación con Probabilidades", size=(1920, 1080))
        
        panel = wx.Panel(self)
        carpeta = os.path.dirname(os.path.abspath(__file__))
        
        # --- SISTEMA DE PROBABILIDADES ---
        suerte = 1  # Forzado para probar; cámbialo por random.randint(1, 100)
        print(f"Número de probabilidad generado: {suerte}")

        # 1. 1% de probabilidad: Carga el video local (Rickrol.mp4)
        if suerte == 1:
            print("¡Evento Raro! 1%: Reproduciendo video.")
            video_path = os.path.join(carpeta, "Rickrol.wmv")
            
            if os.path.exists(video_path):
                # Especificar el backend (útil en Windows)
                try:
                    self.media_ctrl = wx.media.MediaCtrl(
                        panel,
                        size=(1920, 1080),  # Tamaño ajustado a la ventana
                        szBackend=wx.media.MEDIABACKEND_WMP10  # Backend para Windows
                    )
                except Exception:
                    # Si falla el backend específico, usar el predeterminado
                    self.media_ctrl = wx.media.MediaCtrl(panel, size=(480, 270))

                # Vincular el evento de carga para reproducir solo cuando esté listo
                self.media_ctrl.Bind(wx.media.EVT_MEDIA_LOADED, self.on_media_loaded)
                
                if self.media_ctrl.Load(video_path):
                    print("Video cargado. Esperando evento de carga...")
                else:
                    print("Error: No se pudo cargar el video. Verifica el códec o el formato.")
            else:
                print("Aviso: No se encontró el archivo 'Rickrol.mp4'.")

        # 2. 10% de probabilidad: Miku especial
        elif 2 <= suerte <= 11:
            print("¡Evento Poco Común! 10%: Miku especial.")
            self.mostrar_imagen(panel, carpeta, "Miku.jpg", 300, 100)

        # 3. 89% restante: Imagen normal
        else:
            print("¡Evento Normal! 89%: Imagen por defecto.")
            self.mostrar_imagen(panel, carpeta, "Miku.jpg", 200, 150)

        self.Centre()
        self.Show()

    def on_media_loaded(self, event):
        """Se llama cuando el video termina de cargarse."""
        print("Evento EVT_MEDIA_LOADED recibido. Iniciando reproducción.")
        self.media_ctrl.Play()

    def mostrar_imagen(self, panel, carpeta, nombre_archivo, tamano, pos_y):
        """Función auxiliar para mostrar una imagen."""
        img_path = os.path.join(carpeta, nombre_archivo)
        if os.path.exists(img_path):
            image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
            image = image.Scale(tamano, tamano, wx.IMAGE_QUALITY_HIGH)
            self.bitmap = wx.Bitmap(image)
            self.img_ctrl = wx.StaticBitmap(panel, bitmap=self.bitmap, pos=(100, pos_y))

if __name__ == '__main__':
    app = wx.App()
    MiAplicacion()
    app.MainLoop()