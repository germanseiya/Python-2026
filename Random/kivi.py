from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class MiAplicacion(App):
    def build(self):
        self.btn = Button(
            text="¡Hola!",
            font_size=24,
            background_color=(0.1, 0.5, 0.8, 1),
            color=(1, 0, 0, 1)
        )
        
        Window.bind(on_key_down=self._on_keyboard_down)
        
        return self.btn

    def _on_keyboard_down(self, window, key, scancode, codepoint, modifier):
        if codepoint == ' ':
            self.btn.text = "¡Pico pal que lee!"
        
        return True

if __name__ == "__main__":
    MiAplicacion().run()