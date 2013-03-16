import pygame, sys
from pygame.locals import *

def main() :
	"""
	Main Method
	"""
	print("Start main")
	
	#initialize variables
	initialization()
	#Main Game Loop
	runGame()

	print ("End main")
	pygame.quit()

def initialization() :
	"""
	This method initializes the game, loading configurations, reading data, so on and so forth.
	"""
	print("Start initialization")
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Window Title!')
	print("End initialization")
	
def runGame() :
	"""
	This is the main loop of the game. This executes logic in an infinite loop and updates the GUI.
	"""
	print("Start runGame")
	quit = False
	while not quit: # main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				quit = True				
		pygame.display.update()	
	print("End runGame")
	
			
if __name__ == "__main__":
	main()
