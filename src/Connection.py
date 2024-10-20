# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Connection as BaseConnection
from Liquirizia.DataAccessObject.Properties.Cache import Cache

from .Configuration import Configuration

from redis import Redis, ConnectionPool

from typing import Sequence

__all__ = (
	'DataAccessObject'
)


class Connection(BaseConnection, Cache):
	"""Connection Class for Redis"""
	"""
	TODO :
		* Exception Handling with Error of DataAccessObject
	"""

	def __init__(self, conf: Configuration):
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
	
	def setList(self, key, val: Sequence = None):
		from .Types import List
		return List(self, key, val if val else [])
	
	def getList(self, key):
		from .Types import List
		return List(self, key)
