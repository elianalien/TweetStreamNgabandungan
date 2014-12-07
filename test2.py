from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

import os, os.path

Builder.load_file('button.kv')

#window size macpro 15.4": 1440 x 900

class screenLayout(FloatLayout):
	"""docstring for screenLayout"""
	def __init__(self, **kwargs):
		super(screenLayout, self).__init__(**kwargs)
		larrow = Button(
						background_normal='arrows/scroll-left.png',
						background_down='arrows/scroll-left-hit.png',
						size_hint = (0.06,0.1),
						pos_hint={'x':0, 'y':.5}						
						)
		rarrow = Button(
						background_normal='arrows/scroll-right.png',
						background_down='arrows/scroll-right-hit.png',
						size_hint = (0.06,0.1),
						pos_hint={'x':0.93, 'y':.5}						
						)
		self.add_widget(gallery())
		self.add_widget(larrow)
		self.add_widget(rarrow)
		
class gallery(Carousel):
	def __init__(self, **kwargs):
		super(gallery,self).__init__(**kwargs)
		#root = Carousel()
		for i in range(1,5):
			src = "images/%d.png" % i
			images = Image(source=src, 
						   pos=(50, 50), 
						   size=(300, 300),
						   allow_stretch=True)
			self.add_widget(images)	
			#self.add_widget(screenLayout())

class allApp(App):
	def build(self):
		return screenLayout()

if 	__name__ == '__main__':
	allApp().run()