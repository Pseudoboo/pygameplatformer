import sys
sys.path.append('../')
import IMediaLayer
import pygame, sys
from pygame.locals import *

class PyGameMediaLayer(IMediaLayer):
	"""
	Pygame implementation of IMediaLayer
	"""

	def initialize(self):
		"""
		This sets up any basic initialization that the media layer requires.
		"""
		pygame.init()

	def setResolution(self, x, y) :
		"""
		Sets the resolution of the window.
		"""
		DISPLAYSURF = pygame.display.set_mode((x, y))

	def setWindowTitle(self, title) :
		"""
		Sets the title of the window
		"""
		pygame.display.set_caption(title)

	def quit(self) :
		"""
		Teardown for the media layer.
		"""
		pygame.quit()

	def updateDisplay(self) :
		"""
		Updates the display after business logic has repositioned any graphical elements.
		"""
		pygame.display.update()	

	def getEvents(self) :
		"""
		Gets any system events
		"""
		return pygame.event.get()


		