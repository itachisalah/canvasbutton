from kivy.app import App
from kivy.core.window import Window
from kivy.graphics.transformation import Matrix
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from DragableButton import DragableButton
Builder.load_file('Canvas_test_file.kv')
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class Canvas_Test_View(Scatter):

	def doScale(self, scale, touch):
		rescale = self.scale * 1.0 / self.scale
		self.apply_transform(Matrix().scale(rescale, rescale, rescale),
							 post_multiply=True,
							 anchor=self.to_local(touch.x, touch.y))

	def on_touch_down(self, touch):
		if touch.is_mouse_scrolling:
			if touch.button == 'scrolldown':
				## zoom in
				if self.scale < 10:
					self.doScale(self.scale * 1.1, touch);

			elif touch.button == 'scrollup':
				if self.scale > .5:
					self.doScale(self.scale * 0.8, touch);

		super(Canvas_Test_View, self).on_touch_down(touch)
		# Disable multi-touch simulation for my test
		touch.multitouch_sim = False


class Main_app(BoxLayout):
	use_Panarama = False
	imageWidget = None

	def on_button_click(self):
		if (self.use_Panarama):
			self.use_Image("image/level1.jpg")
		else:
			self.use_Image("image/FallPanorama.jpg")
		self.use_Panarama = not self.use_Panarama

	def use_Image(self, imageToUse):

		if self.imageWidget == None:
			self.imageWidget = findWidgetWithID(Window.children[0], 'myid', 'map')
		if self.imageWidget != None:
			self.imageWidget.source = imageToUse

	pass


def findWidgetWithID(starting, property, value):

	for widget in starting.walk():
		if (hasattr(widget, property)):
			if (getattr(widget, property) == value):
				return (widget)


class Canvas_Test(App):
	def build(self):
		Window.clearcolor = (1, 1, 1, 1)
		Window.size = (700,400)
		return Main_app()

if __name__ == '__main__':
	Canvas_Test().run()
