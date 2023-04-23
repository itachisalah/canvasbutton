from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class Mainapp(App):
    def build(self):
        btn = ToggleButton(text="Click Me!!",border=(10,10,10,10),font_size=50,size_hint=(0.5,0.5),pos_hint={"center_x": 0.5,"center_y":0.5})
        return btn

if __name__ == "__main__":
    Mainapp().run()