from abc import abstractmethod
import os.path

from code.configs import config_FileLoader

class FileLoader(object):
	"""Base class for loading files, such as images, sounds etc.

	"""

	# Dir path is specified in derived classes.
	DIR_PATH = os.path.join(os.getcwd(),
							config_FileLoader.RES_DIR)

	@staticmethod
	@abstractmethod
	def load(_filename):
		raise NotImplementedError