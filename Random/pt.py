from kivy.app import App
from kivy.uix.button import Button

class MiAplicacion(App):
    def build(self):
        return Button(
            text="Pico pal que lee!",
            font_size=24,
            background_color=(
                0.1, 0.5, 0.8, 1),
            color=(1, 0, 0, 1)
        )

if __name__ == "__main__":
    MiAplicacion().run()