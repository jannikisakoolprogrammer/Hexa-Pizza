import os.path

import pygame
pygame.init()

from code.classes.FileLoader import FileLoader
from code.configs import config_FileLoaderGraphic

class FileLoaderGraphic(FileLoader):

	DIR_PATH = os.path.join(FileLoader.DIR_PATH,
							config_FileLoaderGraphic.RES_DIR)

	@staticmethod
	def load(_filename):
		filepath = os.path.join(FileLoaderGraphic.DIR_PATH,
								_filename)
		try:
			surface = pygame.image.load(filepath)
			surface = surface.convert_alpha()
			return surface

		except:
			pygame.error("Failed to load '%s'" % filepath)