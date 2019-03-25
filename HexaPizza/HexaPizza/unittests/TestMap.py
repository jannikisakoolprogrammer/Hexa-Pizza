import unittest

import pygame
pygame.init()

from code.classes.Map import Map
from code.configs import config_Town

class TestMap(unittest.TestCase):
	"""Unittest class for testing class 'Map'.

	"""
	def setUp(self):
		window = pygame.display.set_mode((100, 100))


	def tearDown(self):
		pygame.display.quit()


	def testMap(self):
		map1 = Map(config_Town.CONFIG_TOWN1["map_filename"])

		self.assertEqual(map1.__class__.__name__,
						 Map.__name__)

		self.assertGreater(len(map1.tiles), 0)


unittest.main()