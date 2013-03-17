import sys
sys.path.append('ext/impl/')
import pygameinput, pygamemedialayer
from pygameinput import Input
from pygamemedialayer import MediaLayer
"""
This module gets the singletons for outward interfaces.
"""



def getMediaLayer():
	"""
	Gets the media layer.
	"""
	return MediaLayer()
	

def getInput() :
	"""
	Gets the input controller.
	"""
	return Input()