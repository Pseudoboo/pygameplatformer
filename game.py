import sys
sys.path.append('ext')
sys.path.append('ext/impl')
import IMediaLayer
import PyGameMediaLayer
import pygame
from pygame.locals import *
from PyGameMediaLayer import PyGameMediaLayer

MediaLayer = PyGameMediaLayer()


def main() :
	"""
	Main Method
	"""
	print("Start main")
	
	#initialize variables
	initialization()
	#Main Game Loop
	runGame()
	#End
	print ("End main")
	MediaLayer.quit()
	

def initialization() :
	"""
	This method initializes the game, loading configurations, reading data, so on and so forth.
	"""
	print("Start initialization")
	MediaLayer.initialize()
	MediaLayer.setResolution(800, 600)
	MediaLayer.setWindowTitle('Window Title!')
	print("End initialization")
	
def runGame() :
	"""
	This is the main loop of the game. This executes logic in an infinite loop and updates the GUI.
	"""
	print("Start runGame")
	quit = False
	while not quit: # main game loop
		for event in MediaLayer.getEvents():
			if event.type == QUIT:
				quit = True				
		MediaLayer.updateDisplay()
	print("End runGame")
	
			
if __name__ == "__main__":
	main()
