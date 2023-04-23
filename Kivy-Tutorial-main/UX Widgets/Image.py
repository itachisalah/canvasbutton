from kivy.app import App
from kivy.uix.image import Image , AsyncImage

class Main_app(App):
    def build(self):
        image = AsyncImage(source="https://e7.pngegg.com/pngimages/476/159/png-clipart-pokemon-pikachu-pikachu-pokemon-games-pokemon-thumbnail.png",size_hint=(0.5,0.5),pos_hint={'center_x': 0.5,'center_y': 0.5})
        return image


if __name__ == "__main__":
    Main_app().run()