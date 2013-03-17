import sys, pygame
sys.path.append('../')
import imedialayer
from pygame.locals import *
from imedialayer import IMediaLayer

class MediaLayer(IMediaLayer):
	"""
	Pygame implementation of IMediaLayer
	"""

	"""	This clock is used for time based calculations.	"""
	_clock = pygame.time.Clock()
	

	"""Singleton instance"""
	_instance = None

	def __new__(cls, *args, **kwargs):
		"""
		This override insures that this class is a Singleton.
		"""
		if not cls._instance:
			cls._instance = super(MediaLayer, cls).__new__(cls, *args, **kwargs)
		return cls._instance
	


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
		allEvents = pygame.event.get()
		#Filtering out key events because I want them taken care of in pygameinput.
		keyEvents = filter(lambda event: event.type == KEYUP or event.type == KEYDOWN, allEvents)
		events = filter(lambda event: event.type != KEYUP and event.type != KEYDOWN, allEvents)
		#Need to send any input to The input interface.
		return events

	def getDt(self) :
		"""
		Gets the difference in time between two different frames.
		"""
		return self._clock.tick(60)
		