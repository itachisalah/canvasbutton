from kivy.app import App
from kivy.uix.textinput import TextInput

class Mainapp(App):
    def build(self):
        text = TextInput(text="My self Vikas",font_size=100)
        return text

if __name__ == "__main__":
    Mainapp().run()