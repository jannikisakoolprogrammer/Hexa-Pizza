import pygame
pygame.init()

import copy
import math

from code.classes.FileLoaderGraphic import FileLoaderGraphic
from code.configs import config_Scooter

from code.classes.Meadow import Meadow
from code.classes.House import House
from code.classes.Forest import Forest
from code.classes.HexaPizzaHQ import HexaPizzaHQ

class Scooter(pygame.sprite.Sprite):
	def __init__(self,
				 _map,
				 _pos_center_x,
				 _pos_center_y):
		super(Scooter, self).__init__()

		self.degrees = 0
		self.image_orig = FileLoaderGraphic.load(config_Scooter.CONFIG["FILENAME"])
		self.image = pygame.transform.rotate(self.image_orig, self.degrees)
		self.rect = self.image.get_rect()
		self.rect.centerx = _pos_center_x
		self.rect.centery = _pos_center_y

		# Save orig center of map
		self.map_centerx = _map.rect.centerx
		self.map_centery = _map.rect.centery

		self._map = _map

		self.degrees = 0

		self.key_states = {
			"LEFT": False,
			"RIGHT": False,
			"UP": False
			}

		self.collision = False

		self.calc_sin()
		self.calc_cos()

		self.collision_rect = pygame.Rect((0, 0, 10, 10))
		self.collision_rect.center = self.rect.center

		# Make distance bigger.  Edge of scooter.
		self.update_collision_rect()


	def update(self, _eventlist):
		"""Updates the scooter.

		"""
		self.check_update_key_states(_eventlist)
		if self.check_perform_movement():
			self.perform_movement()

	def check_update_key_states(self, _eventlist):
		for event in _eventlist:
			if event.type == pygame.KEYDOWN:
				if event.key == config_Scooter.CONFIG["CONTROLS"]["LEFT"]:
					self.key_states["LEFT"] = True
					self.key_states["RIGHT"] = False
				if event.key == config_Scooter.CONFIG["CONTROLS"]["RIGHT"]:
					self.key_states["LEFT"] = False
					self.key_states["RIGHT"] = True
				if event.key == config_Scooter.CONFIG["CONTROLS"]["UP"]:
					self.key_states["UP"] = True
			if event.type == pygame.KEYUP:
				if event.key == config_Scooter.CONFIG["CONTROLS"]["LEFT"]:
					self.key_states["LEFT"] = False
				if event.key == config_Scooter.CONFIG["CONTROLS"]["RIGHT"]:
					self.key_states["RIGHT"] = False
				if event.key == config_Scooter.CONFIG["CONTROLS"]["UP"]:
					self.key_states["UP"] = False

	
	def check_perform_movement(self):
		for value in self.key_states.values():
			if value == True:
				return True
		return False


	def perform_movement(self):
		"""Moves the map.

		"""
		if self.key_states["LEFT"]:
			# Turn scooter to the left.
			self.alter_angle(config_Scooter.CONFIG["TURN_DEGREES"])
		if self.key_states["RIGHT"]:
			# Turn scooter to the right.
			self.alter_angle(config_Scooter.CONFIG["TURN_DEGREES"] * -1)

		if self.key_states["LEFT"] or self.key_states["RIGHT"]:
			orig_center = self.rect.center
			self.image = pygame.transform.rotate(self.image_orig, self.degrees)
			self.rect = self.image.get_rect()
			self.rect.center = orig_center

		if self.key_states["UP"]:
			if not self.collision:
				# Move map tiles now.  Should use lookup tables here.
				x = self.sin * config_Scooter.CONFIG["SPEED"]
				y = self.cos * config_Scooter.CONFIG["SPEED"]

				self._map.move(x,
							   y)

		self.update_collision_rect()

		# Always check for collisions with meadows, houses, ...
		self.check_collision()


	def alter_angle(self,
					_amount):
		if _amount > 0:
			self.degrees += _amount
			if self.degrees > 360:
				self.degrees = 0 + abs(_amount)

		elif _amount < 0:
			self.degrees += _amount
			if self.degrees < 0:
				self.degrees = 360 + _amount

		self.calc_sin()
		self.calc_cos()


	def calc_sin(self):
		self.sin = math.sin(math.radians(self.degrees))


	def calc_cos(self):
		self.cos = math.cos(math.radians(self.degrees))


	def update_collision_rect(self):
		self.collision_rect.centerx = self.rect.centerx - (self.sin * 40)
		self.collision_rect.centery = self.rect.centery - (self.cos * 40)


	def check_collision(self):
		# Check if there is any collsion between the scooter and various tiles.
		# If there is, set the collision attribute to True.
		# Otherwise set it to False.

		if Meadow.check_collision_with_scooter(self.collision_rect) or \
			Forest.check_collision_with_scooter(self.collision_rect) or \
			House.check_collision_with_scooter(self.collision_rect) or \
			HexaPizzaHQ.check_collision_with_scooter(self.collision_rect):
			self.collision = True
		else:
			self.collision = False