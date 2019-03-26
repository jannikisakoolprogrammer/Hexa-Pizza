import pygame
pygame.init()

import copy
import math

from code.classes.FileLoaderGraphic import FileLoaderGraphic
from code.configs import config_Scooter


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
			# Move map now.  Should use lookup tables here.
			x = math.sin(math.radians(self.degrees)) * config_Scooter.CONFIG["SPEED"]
			y = math.cos(math.radians(self.degrees)) * config_Scooter.CONFIG["SPEED"]

			self.map_centerx += x
			self.map_centery += y

			self._map.rect.centerx = self.map_centerx
			self._map.rect.centery = self.map_centery


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