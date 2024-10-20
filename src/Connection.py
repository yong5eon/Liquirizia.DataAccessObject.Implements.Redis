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
		self.encode = conf.encoder
		self.decode = conf.decoder
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
		return self.connection.keys(str(key))

	def exists(self, key):
		return self.connection.exists(str(key))

	def set(self, key, value, expires=None):
		self.connection.set(str(key), self.encode(value))
		if expires:
			self.connection.expire(str(key), expires)
		else:
			self.connection.persist(str(key))
		return

	def get(self, key):
		return self.decode(self.connection.get(str(key)))

	def expire(self, key, seconds):
		self.connection.expire(str(key), seconds)
		return

	def persist(self, key):
		self.connection.persist(str(key))
		return

	def delete(self, key):
		self.connection.delete(str(key))
		return
	
	def setList(self, key, val: Sequence = None):
		from .Types import List
		return List(self, key, val if val else [])
	
	def getList(self, key):
		from .Types import List
		return List(self, key)
