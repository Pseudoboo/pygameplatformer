import sys
sys.path.append('ext')

import extfactory
import pygame
from pygame.locals import *

MediaLayer = extfactory.getMediaLayer()
Input = extfactory.getInput()


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
		dt = MediaLayer.getDt()

		for event in MediaLayer.getEvents():
			if event.type == QUIT:
				quit = True	
			else:
				print(event)
		MediaLayer.updateDisplay()
	print("End runGame")
	
			
if __name__ == "__main__":
	main()
