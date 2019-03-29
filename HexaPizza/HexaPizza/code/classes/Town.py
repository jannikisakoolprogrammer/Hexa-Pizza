from code.configs import config_Town

from code.classes.FileLoaderTxt import FileLoaderTxt
from code.classes.Map import Map
from code.classes.Scooter import Scooter
from code.configs import config_HexaPizza
from code.classes.Meadow import Meadow

class Town(object):
	def __init__(self,
				 _town_config):
		"""Initialises the instance.

		"""
		self._town_config = _town_config

		self.hexa_pizza = None
		self.scooter = None
		self.houses = []
		self.forests = []
		self.meadows = []

		# First create the town.
		self.create()




	def create(self):
		"""Creates the town.

		"""
		self.map = Map(self._town_config["map_filename"])

		self.scooter = Scooter(self.map,
							   config_HexaPizza.WINDOW_WIDTH / 2,
							   config_HexaPizza.WINDOW_HEIGHT / 2)

		self.create_map_tile_instances()


	def create_map_tile_instances(self):
		map_tile_to_class = self._town_config["mapping_map_tile_class"]

		for t in self.map.tiles:
			if t.char in map_tile_to_class.keys():
				map_tile_to_class[t.char](t)
