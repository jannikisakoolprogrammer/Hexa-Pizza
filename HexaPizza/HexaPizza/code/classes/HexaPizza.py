import pygame
pygame.init()

from code.classes.Town import Town
from code.configs import config_Town

from code.configs import config_HexaPizza
from code.classes.Meadow import Meadow

from code.classes.HexaPizzaHQ import HexaPizzaHQ
from code.classes.House import House

import random

class HexaPizza(object):
	"""Main game class.

	"""
	def __init__(self):
		self.window = pygame.display.set_mode(config_HexaPizza.WINDOW_DIMENSIONS,
											  config_HexaPizza.FLAGS_MODE)
		self.clock = pygame.time.Clock()

	def main_game(self):
		self.town = Town(config_Town.CONFIG_TOWN1)

		hexa_pizza_hq = HexaPizzaHQ.Instances[0]

		running = True
		while running:
			eventlist = pygame.event.get()
			for e in eventlist:
				if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
					pass

			# Update Player/Scooter
			self.town.scooter.update(eventlist)

			#if hexa_pizza_hq.show_main_menu:
			hexa_pizza_hq.hexa_pizza_hq_menu.update(eventlist)

			# Updates houses.
			for h in House.Instances:
				h.update(self.town.scooter, hexa_pizza_hq.hexa_pizza_log)

			self.window.blit(self.town.map.image,
							 self.town.map.rect)

			self.window.blit(self.town.scooter.image,
							 self.town.scooter.rect)

			hexa_pizza_hq.hexa_pizza_hq_menu.draw(self.window)
			hexa_pizza_hq.hexa_pizza_log.draw(self.window)

			pygame.display.update()
			self.clock.tick(config_HexaPizza.FPS)

		pygame.display.quit()