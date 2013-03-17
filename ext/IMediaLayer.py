import abc

class IMediaLayer(object):
	"""
	This is an abstraction layer for the media layer used.
	In case I find pygame unsuitable, I want a way to make it easier to remove it from the code.

	"""
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def initialize(self):
		"""
		This sets up any basic initialization that the media layer requires.
		"""
		raise NotImplementedError

	@abc.abstractmethod
	def setResolution(self, x, y) :
		"""
		Sets the resolution of the window.
		"""
		raise NotImplementedError

	@abc.abstractmethod
	def setWindowTitle(self, title) :
		"""
		Sets the title of the window
		"""
		raise NotImplementedError

	@abc.abstractmethod
	def quit(self) :
		"""
		Teardown for the media layer.
		"""
		raise NotImplementedError

	@abc.abstractmethod
	def updateDisplay(self) :
		"""
		Updates the display after business logic has repositioned any graphical elements.
		"""
		raise NotImplementedError

	@abc.abstractmethod
	def getEvents(self) :
		"""
		Gets any system events
		"""
		raise NotImplementedError






