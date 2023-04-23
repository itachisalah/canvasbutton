from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.label import Label

class Mainapp(App):
    def build(self):
        layout = PageLayout()
        layout.add_widget(Label(text="My self vikas", color=(1, 0, 0, 1), bold=True))
        layout.add_widget(Label(text="I am boy", color=(0, 1, 0, 1), bold=True))
        layout.add_widget(Label(text="B.tech Student", color=(0, 0, 1, 1), bold=True))
        layout.add_widget(Label(text="From NSUT", color=(1, 1, 1, 1), bold=True))
        return layout

if __name__ == "__main__":
    Mainapp().run()