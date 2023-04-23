from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Mainapp(App):
    def build(self):
        layout = GridLayout(cols=2)

        layout.add_widget(Button(text="Button 1"))
        layout.add_widget(Button(text="Button 2"))
        layout.add_widget(Button(text="Button 3"))
        layout.add_widget(Button(text="Button 4"))
        return layout

if __name__ == "__main__":
    Mainapp().run()