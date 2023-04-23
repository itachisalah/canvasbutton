from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class Mainapp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",spacing=10,padding=10)
        l = Label(text="Enter your name : ",font_size=100,bold=True)
        t = TextInput(font_size=100)
        layout.add_widget(l)
        layout.add_widget(t)
        return layout

if __name__ == "__main__":
    Mainapp().run()