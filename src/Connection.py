# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Connection as BaseConnection
from Liquirizia.DataAccessObject.Properties.Cache import Cache

from .Configuration import Configuration, ConnectionType

from collections.abc import Sequence, Set, Mapping

from redis import (
	Redis, 
	ConnectionPool,
)
from redis.cluster import (
	RedisCluster,
	ClusterNode,
)

__all__ = (
	'Connection',
)


class Connection(BaseConnection, Cache):
	"""Connection Class for Redis"""

	def __init__(self, conf: Configuration):
		self.conf = conf
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
		# TODO : connect from url
		if self.conf.type == ConnectionType.Cluster:
			self.connection = RedisCluster.from_url(
				self.conf.url, 
				decode_responses=True,
				require_full_coverage=True,
			)
		if self.conf.type == ConnectionType.Pool:
			if not self.pool:
				self.pool = ConnectionPool.from_url(self.conf.url, decode_responses=True)
			self.connection = Redis(connection_pool=self.pool)
		if not self.connection:	
			self.connection = Redis.from_url(self.conf.url, decode_responses=True)
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
	
	def setList(self, key, val: Sequence = None) -> Sequence:
		from .Types import List
		return List(self, key, val if val else [])
	
	def getList(self, key) -> Sequence:
		from .Types import List
		return List(self, key)

	def setSet(self, key, val: Set = None) -> Set:
		from .Types import Set
		return Set(self, key, val if val else [])
	
	def getSet(self, key) -> Set:
		from .Types import Set
		return Set(self, key)

	def setSortedSet(self, key, val: Set = None) -> Set:
		from .Types import SortedSet
		return SortedSet(self, key, val if val else [])
	
	def getSortedSet(self, key) -> Set:
		from .Types import SortedSet
		return SortedSet(self, key)

	def setHash(self, key, val: Mapping= None) -> Mapping:
		from .Types import Hash 
		return Hash(self, key, val if val else {})
	
	def getHash(self, key) -> Mapping:
		from .Types import Hash
		return Hash(self, key)
