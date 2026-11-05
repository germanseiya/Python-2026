from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

class MiAplicacion(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        
        self.img = Image(source='Romance bajo un cielo de flores y estrellas (Miku).png', size_hint=(1, 0.6))
        
        self.btn = Button(
            text="¡Presiona Espacio!",
            font_size=24,
            size_hint=(1, 0.4),
            background_color=(0.1, 0.5, 0.8, 1),
            color=(1, 0, 0, 1)
        )
        
        layout.add_widget(self.img)
        layout.add_widget(self.btn)
        
        self.sound = SoundLoader.load('Warmness On The Soul.mp3')
        
        Window.bind(on_key_down=self._on_keyboard_down)
        
        return layout

    def _on_keyboard_down(self, window, key, scancode, codepoint, modifier):
        if codepoint == ' ':
            self.btn.text = "¡Espacio presionado, música activa!"
            
            if self.sound:
                self.sound.play()
                
        return True

if __name__ == "__main__":
    MiAplicacion().run()