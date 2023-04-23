from kivy.app import App
from kivy.uix.slider import Slider

class Mainapp(App):
    def build(self):
        sl = Slider(orientation="vertical",value_track=True,value_track_color=(1,0,0,1))
        return sl

if __name__ == "__main__":
    Mainapp().run()