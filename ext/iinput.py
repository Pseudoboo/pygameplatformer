class IInput(object):
	"""
	This is an abstraction layer for capturing input and converting it to game logic
	"""

	def getKeysPressed(self):
		"""
		This sets up any basic initialization that the media layer requires.
		"""
		raise NotImplementedError