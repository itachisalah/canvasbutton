from kivy.app import App
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox

Window.clearcolor = (1,1,1,1)

class Main_app(App):
    def build(self):
        def on_check_box(check,value):
            if value:
                print("The CheckBox ",check," is active")
            else:
                print("The Checkbox ",check," is inactive")
        checkbox = CheckBox(color=(0,0,1,1),size_hint=(0.4,0.4),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        checkbox.bind(active=on_check_box)
        return checkbox

if __name__ == "__main__":
    Main_app().run()