import unittest

import pygame
pygame.init()

from code.classes.FileLoaderTxt import FileLoaderTxt

class TestFileLoaderTxt(unittest.TestCase):
	"""Unit test class for class 'FileLoaderTxt'.

	"""
	def setUp(self):
		window = pygame.display.set_mode((100, 100))

	def tearDown(self):
		pygame.quit()

	def test_load(self):
		f = FileLoaderTxt.load("Town1.txt")
		self.assertEqual(f.__class__.__name__, list.__name__)

	def test_load2(self):
		self.assertRaises(FileNotFoundError, FileLoaderTxt.load("blabla.txt"))

unittest.main()
