class IInput(object):
	"""
	This is an abstraction layer for capturing input and converting it to game logic
	"""

	def getChangedKeys(self):
		"""
		Gets a list of the keys that are newly pressed.
		"""
		raise NotImplementedError

class KeyState:
	"""
	An enumeration for the state of keys, whether up or down.
	"""
	Down = 0
	Up = 1