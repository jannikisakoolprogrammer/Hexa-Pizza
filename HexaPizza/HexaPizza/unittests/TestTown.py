import unittest

import pygame
pygame.init()

from code.classes.Town import Town
from code.classes.Map import Map

from code.configs import config_Town

class TestTown(unittest.TestCase):
	"""Unit test class for class 'Town'.

	"""
	def setUp(self):
		window = pygame.display.set_mode((100, 100))


	def tearDown(self):
		pygame.quit()

	
	def testTown(self):
		town = Town(config_Town.CONFIG_TOWN1)
		self.assertEqual(town.__class__.__name__,
						 Town.__name__)

		self.assertEqual(town.map.__class__.__name__,
						 Map.__name__)


unittest.main()