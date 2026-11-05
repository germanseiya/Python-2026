from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

class MiAplicacion(App):
    def build(self):
        # Usamos FloatLayout para posicionar los elementos con precisión
        layout = FloatLayout()
        
        # 1. Imagen centrada, adaptada y manteniendo proporciones
        self.img = Image(
            source='Romance bajo un cielo de flores y estrellas (Miku).png',
            size_hint=(1.0, 1.0),                      # Ocupa el 80% del ancho y alto
            pos_hint={'center_x': 0.5, 'center_y': 0.5}, # Centrada exactamente en la mitad
            allow_stretch=True,                        # Permite que la imagen se redimensione
            keep_ratio=True                            # Evita que se estire o deforme
        )
        
        # 2. Botón ubicado en la parte inferior central
        self.btn = Button(
            text="¡Presiona Espacio!",
            font_size=24,
            size_hint=(0.6, 0.12),                     # Ancho y alto proporcionales
            pos_hint={'center_x': 0.5, 'y': 0.05},     # Centrado horizontalmente y pegado abajo
            background_color=(0.1, 0.5, 0.8, 1),
            color=(1, 0, 0, 1)
        )
        
        layout.add_widget(self.img)
        layout.add_widget(self.btn)
        
        # Cargar música y eventos
        self.sound = SoundLoader.load('Warmness On The Soul.mp3')
        Window.bind(on_key_down=self._on_keyboard_down)
        
        return layout

    def _on_keyboard_down(self, window, key, scancode, codepoint, modifier):
        if codepoint == ' ':
            if self.sound:
                self.sound.play()
        return True

if __name__ == "__main__":
    MiAplicacion().run()