import display
import pygame
import os

WIDTH  = 25
HEIGHT = 25

# 30 tiles wide
# I need a better way of mapping this,
# so doing it on a grid will perhaps
# look decent.
# As it is, this is only really good
# for reference.
tile_mapping = {
	"ceiling" : (
		30, # Starting tile
		86, # Ending tile
	),
	"walls" : (
		# List of wall tiles
		120, 121, 122, 123, 124, 125, 126,
		150, 151, 152, 153, 154, 155, 156,
	),
	"wall_stairs" : (
		# List of wall stairs tiles
		127,
		157,
	),
	"wall_doorway" : (
		# List of wall doorway tiles
		128,
		158,
	),
	"floor" : (
		210, # Starting tile
		281, # Ending tile
	),
# Good for the demo, but might want to add
# mapping for the rest of the file eventually.
}

class Map(display.Renderable):
	''' Map class

	   Tracks the map data
	'''

	def __init__(self, size, sprite_map, offset=(0,0)):
		''' Constructor

		size -- the width and height of the map as a tuple
		sprite_map -- a Pygame Surface object containing
		              the sprite graphics for map tiles
		offset -- the position of the upper left corner
		          as a tuple, for rendering
		'''
		super(type(self), self).__init__(sprite_map, -1)
		self._map = [0 for i in range(size[0] * size[1])]
		self.size = size
		self.offset = offset

	def render(self, screen):
		for n, tile in enumerate(self._map):
			x = (n % self.size[0]) * 32 + self.offset[0]
			y = (n / self.size[0]) * 32 + self.offset[1]
			tx = (tile % 30) * 16
			ty = (tile / 30) * 16

			screen.blit(
				pygame.transform.scale(
					self.sprite_map.subsurface(
						pygame.Rect(tx, ty, 16, 16)
					),
					(32, 32)
				),
				(x, y),
			)

	def __getitem__(self, (x, y)):
		try:
			return self._map[x + y * self.size[0]]
		except IndexError as e:
			e.args = ("Map index out of range",)
			e.message = "Map index out of range"
			raise

	def __setitem__(self, (x, y), value):
		try:
			self._map[x + y * self.size[0]] = value
		except IndexError as e:
			e.args = ("Map index out of range",)
			e.message = "Map index out of range"
			raise

	def set_map(self, map):
		''' Set the map to a given list

		map -- This is a list of ints mapping to the
		       sprite image.  It must be a list that
		       is exactly the same length as self._map.
		'''

		if type(map) is not list:
			raise Exception("argument is not a list")

		if len(map) == len(self._map):
			self._map = map
		else:
			raise Exception("Map size does not match list size")

def sample_map():
	m = Map(
		(10, 10),
	        display.get_image(
			os.path.join(
				'img',
				'dungeon tileset calciumtrice.png'
			)
		),
		offset=(16*2, 16*2)
	)

	tiles = [
		82,  41,  41,  42,  43,  41,  43,  43,  42, 81,
		44, 124, 122, 121, 123, 124, 128, 123, 127, 36,
		45, 154, 152, 151, 153, 154, 158, 153, 157, 35,
		44, 211, 219, 220, 220, 218, 219, 218, 212, 37,
		44, 216, 271, 273, 271, 271, 272, 278, 226, 37,
		46, 217, 272, 274, 272, 274, 273, 272, 224, 37,
		46, 215, 271, 271, 272, 271, 271, 271, 226, 36,
		45, 216, 271, 271, 274, 273, 277, 274, 225, 35,
		44, 215, 272, 273, 271, 273, 272, 273, 224, 35,
		80,  38,  39,  40,  40,  38,  39,  38,  40, 79,
	]

	m.set_map(tiles)
	return m

''' Tile Mappings

Ceiling:
	blank		30

	bottom_right_inside_corner	79
	bottom_left_inside_corner	80
	top_right_inside_corner		81
	top_left_inside_corner		82

	right_edge	35, 36, 37
	bottom edge	38, 39, 40
	top_edge	41, 42, 43
	left_edge	44, 45, 46

Floor:
	blank	210

	normal		271, 272, 273, 274
	decorative	275, 276, 277, 278
	stone_tile	279, 280, 281

	top_left_outside_corner		211
	top_right_outside_corner	212
	bottom_left_outside_corner	213
	bottom_right_outside_corner	214

	left_edge	215, 216, 217
	top_edge	218, 219, 220
	bottom_edge	221, 222, 223
	right_edge	224, 225, 226

Wall:
	normal			123, 124
				153, 154

	left_outside_corner	120
				150
	right_outside_corner	125
				155
	double_outside_corner	126
				156

	with_bumps		121
				151
	with_crack		122
				152

	with_stairs		127
				157

	with_doorway		128
				158
	
'''
