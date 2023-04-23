from kivy.app import App
from kivy.uix.button import Button

class Main_app(App):
    def build(self):
        button = Button(text="Click Me!!",font_size=70,size_hint=(0.5,0.5),pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_press=self.btnpressed)
        return button

    def btnpressed(self,instance):
        print("Button pressed")

if __name__ == "__main__":
    Main_app().run()