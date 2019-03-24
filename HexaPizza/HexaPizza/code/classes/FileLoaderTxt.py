import os.path

from code.classes.FileLoader import FileLoader
from code.configs import config_FileLoaderTxt

class FileLoaderTxt(FileLoader):
	"""File loader for loading text files.

	"""

	DIR_PATH = os.path.join(FileLoader.DIR_PATH,
							config_FileLoaderTxt.RES_DIR)

	def load(_filename):
		"""Loads a text file and returns the content as a string
		of lines.

		"""
		filepath = os.path.join(FileLoaderTxt.DIR_PATH,
							    _filename)
		try:
			with open(filepath, "r") as f:
				file_lines = f.read().splitlines()
				return file_lines

		except FileNotFoundError:
			print("Could not read file '%s'" % filepath)