from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

class MiAplicacion(App):
    def build(self):
        layout = FloatLayout()
        
        self.img = Image(
            source='Romance bajo un cielo de flores y estrellas (Miku).png',
            size_hint=(1.0, 1.0),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            allow_stretch=True,
            keep_ratio=True
        )
        
        self.btn = Button(
            text="¡Presiona Espacio!",
            font_size=24,
            size_hint=(0.6, 0.12),
            pos_hint={'center_x': 0.5, 'y': 0.05},
            background_color=(0.1, 0.5, 0.8, 1),
            color=(1, 0, 0, 1)
        )
        self.btn.opacity = 0
        
        layout.add_widget(self.img)
        layout.add_widget(self.btn)
        
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