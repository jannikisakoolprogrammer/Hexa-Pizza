from code.configs import config_Town

from code.classes.FileLoaderTxt import FileLoaderTxt
from code.classes.Map import Map

class Town(object):
	def __init__(self,
				 _town_config):
		"""Initialises the instance.

		"""
		self._town_config = _town_config

		# First create the town.
		self.create()


	def create(self):
		"""Creates the town.

		"""
		self.map = Map(self._town_config["map_filename"])
