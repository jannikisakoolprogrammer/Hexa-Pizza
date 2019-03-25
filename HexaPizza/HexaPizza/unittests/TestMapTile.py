import unittest

import pygame
pygame.init()

from code.classes.MapTile import MapTile
from code.configs import config_MapTile

class TestMapTile(unittest.TestCase):
	"""Unit test class for class 'MapTile'.

	"""
	def setUp(self):
		window = pygame.display.set_mode((100, 100))

	
	def tearDown(self):
		pygame.display.quit()


	def testMapTile(self):
		mapTile = MapTile(config_MapTile.SCENERY_FOREST_VARIATION_1,
						  0,
						  0)

		self.assertEqual(mapTile.__class__.__name__,
						 MapTile.__name__)

		self.assertEqual(mapTile.char,
						 config_MapTile.SCENERY_FOREST_VARIATION_1)


unittest.main()
