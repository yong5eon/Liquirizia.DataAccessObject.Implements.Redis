# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import DataAccessObjectConfiguration as DataAccessObjectConfigurationBase

__all__ = (
	'DataAccessObjectConfiguration'
)


class DataAccessObjectConfiguration(DataAccessObjectConfigurationBase):
	"""
	Data Access Object Configuration Class for Redis
	"""

	def __init__(self, host, port=6379, username=None, password=None, max=3, persistent=True):
		self.host = host
		self.port = port
		self.user = username
		self.password = password
		self.max = max
		self.persist = persistent
		return
