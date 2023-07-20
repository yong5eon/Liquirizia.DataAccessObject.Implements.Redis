# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import DataAccessObject as DataAccessObjectBase
from Liquirizia.DataAccessObject.Properties.Cache import Cache

from .DataAccessObjectConfiguration import DataAccessObjectConfiguration

from redis import Redis, ConnectionPool

__all__ = (
	'DataAccessObject'
)


class DataAccessObject(DataAccessObjectBase, Cache):
	"""
	Data Access Object Class for Redis

	TODO :
		* Exception Handling with DataAccessObjectError
	"""

	def __init__(self, conf: DataAccessObjectConfiguration):
		if conf.persist:
			self.pool = ConnectionPool(host=conf.host, port=conf.port, max_connections=conf.max, decode_responses=True)
		else:
			self.pool = None
		self.connection = None
		return

	def __del__(self):
		if self.connection:
			self.close()
		return

	def connect(self):
		if self.pool:
			self.connection = Redis(connection_pool=self.pool)
		else:
			self.connection = Redis(host=self.conf.host, port=self.conf.port, decode_responses=True)
		return

	def close(self):
		self.connection.close()
		return

	def keys(self, key):
		return self.connection.keys(key)

	def exists(self, key):
		return self.connection.exists(key)

	def set(self, key, value, expires=None):
		self.connection.set(key, value)
		if expires:
			self.connection.expire(key, expires)
		else:
			self.connection.persist(key)
		return

	def get(self, key):
		return self.connection.get(key)

	def expire(self, key, seconds):
		self.connection.expire(key, seconds)
		return

	def persist(self, key):
		self.connection.persist(key)
		return

	def delete(self, key):
		self.connection.delete(key)
		return
