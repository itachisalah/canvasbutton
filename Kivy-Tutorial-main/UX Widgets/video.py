from kivy.app import App
from kivy.uix.video import Video 

class Mainapp(App):
    def build(self):
        v = Video(source="https://www.youtube.com/watch?v=eVVaqFDG6Fo&list=RDeVVaqFDG6Fo&start_radio=1",play=True)
        return v

if __name__ == "__main__":
    Mainapp().run()