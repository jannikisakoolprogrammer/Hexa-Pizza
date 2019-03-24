import unittest
from code.classes.FileLoaderGraphic import FileLoaderGraphic

import pygame
pygame.init()

class TestFileLoaderGraphic(unittest.TestCase):

	def setUp(self):
		window = pygame.display.set_mode((100, 100))
		pass

	def tearDown(self):
		pygame.quit()

	def test_load(self):
		img = FileLoaderGraphic.load("image.png")
		self.assertEqual(img.__class__.__name__, pygame.Surface.__name__)

	def test_load2(self):
		self.assertRaises(pygame.error, FileLoaderGraphic.load("blabla.png"))

unittest.main()