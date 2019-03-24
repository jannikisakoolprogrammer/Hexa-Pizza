import pygame
pygame.init()

from code.classes.FileLoaderGraphic import FileLoaderGraphic
from code.configs import config_MapTile

class MapTile(pygame.sprite.Sprite):
	"""Represents a tile of a map.
	This is an abstract class, derive from this class.
	
	"""
	# This is for storing already loaded files so we don't have to load them twice if
	# required.
	FILES = {}

	def __init__(self,
				 _char,
				 _pos_left,
				 _pos_top):
		super(MapTile, self).__init__()

		# Fetch the filenames by using the char passed.
		filenames = config_MapTile.MAPPING_CHAR_FILENAMES[_char]
		
		# Check whether the file already is contained in FILES
		for f in filenames.values():
			if f not in MapTile.FILES:
				# Load file first
				MapTile.FILES[f] = FileLoaderGraphic.load(f)

		self.image_day = MapTile.FILES[filenames[config_MapTile.DAY_IMAGE]]
		self.image_night = MapTile.FILES[filenames[config_MapTile.NIGHT_IMAGE]]

		# Daytime image is always set as default.
		self.image = self.image_day
		self.rect = self.image.get_rect()

		self.rect.left = _pos_left
		self.rect.top = _pos_top

		self.char = _char # For identifying the type of tile for later use.