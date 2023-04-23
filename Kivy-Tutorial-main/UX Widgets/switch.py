from kivy.app import App
from kivy.uix.switch import Switch

class Mainapp(App):
    def build(self):
        def on_switch(check,value):
            if value:
                print("ON!!")
            else:
                print("OFF!!")

        s = Switch()
        s.bind(active=on_switch)
        return s

if __name__ == "__main__":
    Mainapp().run()