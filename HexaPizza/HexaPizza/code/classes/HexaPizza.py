import pygame
pygame.init()

from code.classes.Town import Town
from code.configs import config_Town

from code.configs import config_HexaPizza

class HexaPizza(object):
	"""Main game class.

	"""
	def __init__(self):
		self.window = pygame.display.set_mode(config_HexaPizza.WINDOW_DIMENSIONS,
											  config_HexaPizza.FLAGS_MODE)
		self.clock = pygame.time.Clock()

	def main_game(self):
		self.town = Town(config_Town.CONFIG_TOWN1)

		running = True
		while running:
			eventlist = pygame.event.get()
			for e in eventlist:
				if e.type == pygame.KEYDOWN:
					running = False
			self.window.blit(self.town.map.image,
							 self.town.map.rect)
			pygame.display.update()
			self.clock.tick(config_HexaPizza.FPS)

		pygame.display.quit()