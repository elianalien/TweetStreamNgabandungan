import os, sys, random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.moretransitions import BlurTransition
from kivy.properties import StringProperty

class Page(Screen):
	source = StringProperty()

class SlideShow(App):

	def build(self):
		
		rootPath = os.path.dirname(os.path.realpath(sys.argv[0]))
		
		self.photos = []
		for image in os.listdir(rootPath + '/Photos'):
			self.photos.append(rootPath + '/Photos/' + image)

		self.screenManager = ScreenManager(transition=BlurTransition(duration=1.0))

		self.page1 = Page(name='page1', source = self.photos[0])
		self.page2 = Page(name='page2', source = self.photos[1])
		self.page3 = Page(name='page3', source = self.photos[2])
		self.index = 0
		
		self.screenManager.add_widget(self.page1)
		self.screenManager.add_widget(self.page2)
		self.screenManager.add_widget(self.page3)
		
		return self.screenManager
		
	def next(self,*largs):
				
		if(self.screenManager.current == 'page1'):
			next = 'page2'
			page = self.page2
		else:
			next = 'page1'
			page = self.page1
			
		self.index += 1
		if self.index == len(self.photos):
			self.index = 0
		page.source = self.photos[self.index]
		page.background.scale = 1.0		
		self.screenManager.current = next
	
	def prev(self,*largs):
		if(self.screenManager.current == 'page1'):
			prev = 'page2'
			page = self.page2
		else:
			prev = 'page1'
			page = self.page1
			
		self.index -= 1
		if self.index == len(self.photos):
			self.index = 0
		page.source = self.photos[self.index]
		page.background.scale = 1.0		
		self.screenManager.current = prev

if __name__ in '__main__':
	SlideShow().run()
