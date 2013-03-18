import sys
sys.path.append('../')
import iinput
import pygame, sys
from pygame.locals import *
from iinput import IInput, KeyState


"""
A List of the type of events that the media layer cares about.
This is a constant for the get events method.
"""
_events = [
	KEYDOWN, 
	KEYUP,
	MOUSEMOTION,
	MOUSEBUTTONUP,
	MOUSEBUTTONDOWN,
	JOYAXISMOTION,
	JOYBALLMOTION,
	JOYHATMOTION,
	JOYBUTTONUP,
	JOYBUTTONDOWN]

class Input(IInput):
	"""
	This is an abstraction layer for capturing input and converting it to game logic
	"""

	"""Singleton instance"""
	_instance = None

	def __new__(cls, *args, **kwargs):
		"""
		This override insures that this class is a Singleton.
		"""
		if not cls._instance:
			cls._instance = super(Input, cls).__new__(	cls, *args, **kwargs)
		return cls._instance

	def getChangedKeys(self):
		"""
		Gets a list of newly depressed keys.
		"""
		events = pygame.event.get(_events)
		returnValue = list()

		keyUpEvents = filter(lambda event: event.type == KEYUP, events)
		returnValue.extend(map(lambda event: (KeyState.Up, pygame.key.name(event.key)), keyUpEvents))

		keyDownEvents = filter(lambda event: event.type == KEYDOWN, events)
		returnValue.extend(map(lambda event: (KeyState.Down, pygame.key.name(event.key)), keyDownEvents))

		return returnValue