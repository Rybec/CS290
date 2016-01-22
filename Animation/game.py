import sys
import pygame

import display
import ehandler
import objects
import map

WIDTH  = 384
HEIGHT = 384

# Event handlers
def quit(e):
	'''Event hander for quit events'''
# Any shutdown code should go here
	sys.exit()


pygame.display.init()

display.init(WIDTH, HEIGHT)
display.register(map.sample_map())
display.register(objects.sample_statue())

minotaur = objects.sample_minotaur()
display.register(minotaur)

ehandler.register("quit", quit)

while True:
	minotaur.update()
	display.render()
	ehandler.run()



pygame.quit()
