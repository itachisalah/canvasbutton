from kivy.app import App
from kivy.uix.label import Label

class Main_app(App):
    def build(self):
        label = Label(text="My Self Vikas",bold=True,italic=True,font_size=100)
        return label

if __name__ == "__main__":
    Main_app().run()