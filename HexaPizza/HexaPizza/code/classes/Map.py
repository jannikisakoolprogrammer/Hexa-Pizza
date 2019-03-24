import pygame
pygame.init()

from code.classes.MapTile import MapTile
from code.configs import config_MapTile

from code.classes.FileLoaderTxt import FileLoaderTxt

class Map(pygame.sprite.Sprite):
	"""Represents the map of the town.
	This will be used as background.

	"""
	def __init__(self,
				 _file_map):
		super(Map, self).__init__()

		self.tiles = pygame.sprite.Group()

		# Store map for future reference
		self.map = FileLoaderTxt.load(_file_map)

		# We need max width and height for pygame.Surface.
		self.image = pygame.Surface(self.calc_map_dimensions_in_px())
		self.rect = self.image.get_rect()

		# Now create tile instances, e.g., draw on the map.
		self.create_map_tiles()

		# Now blit the map tiles' surfaces onto the map.
		self.tiles.draw(self.image)

	
	def calc_map_width_in_px(self):
		return (max([len(x) for x in self.map])) * config_MapTile.MAP_TILE_SIZE_WIDTH


	def calc_map_height_in_px(self):
		return len([len(x) for x in self.map]) * config_MapTile.MAP_TILE_SIZE_HEIGHT


	def calc_map_dimensions_in_px(self):
		return self.calc_map_width_in_px(), self.calc_map_height_in_px()


	def create_map_tiles(self):
		"""Create map tiles.

		"""
		left = top = 0

		for line in self.map:
			for tile in line:
				self.tiles.add(MapTile(tile,
									   left,
									   top))
				left += config_MapTile.MAP_TILE_SIZE_WIDTH

			top += config_MapTile.MAP_TILE_SIZE_HEIGHT
			left = 0