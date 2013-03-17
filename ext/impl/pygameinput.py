import sys
sys.path.append('../')
import iinput
import pygame, sys
from pygame.locals import *
from iinput import IInput



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

	def getKeysPressed(self):
		"""
		This sets up any basic initialization that the media layer requires.
		"""
		raise NotImplementedError