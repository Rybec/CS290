import display
import pygame
import os

class Object(display.Renderable):
	'''Class for in-game objects

	Note that this is different from the built-in
	object class.  Python is case sensitive.
	'object' refers to the built-in class, which
	should be the ancestor of all objects.  'Object'
	is the base class for everything in the game
	that is not a map tile.
	'''

	def __init__(self, sprite_map):
		# Call the parent constructor
		super(Object, self).__init__(sprite_map, 0)

		self.tile = (0, 0)	# Location in tile units as float

	def render(self, screen):
		''' Override in children'''
		pass

	def set_location(self, x, y):
		''' Set the location of the object

		x, y -- location in floating point tile units
		'''

		self.tile = (x, y)

		# Update the z-index
		self.z_index = self.tile[1] * 100


class HeroStatue(Object):
	''' Static hero statue'''

	def __init__(self):
		# Call the parent constructor
		super(HeroStatue, self).__init__(
			display.get_image(
				os.path.join(
					'img',
					'dungeon tileset calciumtrice.png'
				)
			)
		)

	def render(self, screen):
		''' Renders the hero statue'''

		x = int(self.tile[0] * 32)
		y = int(self.tile[1] * 32)

		screen.blit(
			pygame.transform.scale(
				self.sprite_map.subsurface(
					pygame.Rect(
						304, 304,
						16, 32
					),
				),
				(32, 64)
			),
			(x, y - 32)
		)

class Actions(object):
	''' Action state enum'''
	IDLE   = 0
	TAUNT  = 1
	WALK   = 2
	ATTACK = 3
	DIE    = 4


class Minotaur(Object):
	''' Minotaur character'''

#!!! Really, there should be a Mobile object that
#!!! this inherits from.  The Mobile object would
#!!! handle movement.  This would set the movement
#!!! speed and deal with the rendering details.

	# This is essentially a static class variable
	# It contains the mapping of frames in the
	# minotaur sprite map.
	frames = {
		Actions.IDLE   : [(i * 48,   0) for i in range(10)],
		Actions.TAUNT  : [(i * 48,  48) for i in range(10)],
		Actions.WALK   : [(i * 48,  96) for i in range(10)],
		Actions.ATTACK : [(i * 48, 144) for i in range(10)],
		Actions.DIE    : [(i * 48, 192) for i in range(10)],
	}

	def __init__(self):
		# Call the parent constructor
		super(Minotaur, self).__init__(
			display.get_image(
				os.path.join(
					'img',
					'minotaur spritesheet calciumtrice.png'
				)
			)
		)
		self.clock = pygame.time.Clock()
		self.frame = 0.0

	def render(self, screen):
		''' Renders the minotaur'''

		# Convert tile/subtile to screen coordinates
		x = int(self.tile[0] * 32)
		y = int(self.tile[1] * 32)

		self.frame = (self.frame + (self.clock.tick() / 100.0)) % 10

		screen.blit(
		    pygame.transform.scale(
		        self.sprite_map.subsurface(
		            pygame.Rect(
		                self.frames[Actions.ATTACK][int(self.frame)],
		                (48, 48)
		            ),
		        ),
		        (96, 96)
		    ),
		    (x - 40, y - 64)
		)

	def update(self):
		''' This gets called every game loop'''
		pass



def sample_statue():
	s = HeroStatue()
	s.set_location(3, 5)
	return s

def sample_minotaur():
	m = Minotaur()
	m.set_location(4.5, 5)
	return m
