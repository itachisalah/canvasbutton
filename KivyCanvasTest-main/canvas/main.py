from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.scatter import Scatter
from DragableButton import DragableButton
from kivy.config import Config
from kivy.graphics.transformation import Matrix

Config.set('input','mouse','mouse,multitouch_on_demand')

Builder.load_file('Canvas_test_file.kv')


class Canvas_Test_View(Scatter):
    def doScale(self, scale, touch):
        rescale= self.scale *1 / self.scale
        self.ply_transfrom(Matrix().scale(rescale, rescale, rescale),
                           post_multiply=True,
                           anchor=self.to_local(touch.x,touch.y))
        
        
        
    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if self.scale < 10:
                    self.doScale(self.scale * 1.1, touch)
            elif touch.button == 'scrollup':
                if self.scale > 0.5:
                    self.doScale(self.scale *0.8 ,touch)
            
        super(Canvas_Test_View,self).on_touch_down(touch)
        touch.multitouch_sim = False

class Main_app(BoxLayout):
    use_Panarma= False
    imageWidget =None
    
    def on_button_click(self):
        if (self.use_Panarma):
            self.use_image('image/xman.jpg')
        else:
            self.use_image('image/heroy.jpg')
        self.use_Panarma= not self.use_Panarma

    def use_image(self, imageToUse):
        if self.imageWidget== None:
            self.imageWidget= findWidgetWidthID(Window.children[0], 'myid','map')
        if self.imageWidget != None:
            self.imageWidget.source= imageToUse
    pass
        

def findWidgetWidthID(starting, property, value):
    for widget in starting.walk():
        if (hasattr(widget,property)):
            if(getattr(widget,property)==value):
                return(widget)


class Canvas_Test(App):
    def build(self):
        Window.size= 700,400
        Window.clearcolor=(1,1,1,1)
        
        return Main_app()


if __name__=="__main__":
    
    Canvas_Test().run()