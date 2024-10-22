# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import MutableMapping, Mapping

__all__ = (
	'Hash'
)


class Hash(Type, MutableMapping):
	"""Type Helper Class for Hash"""

	def __init__(self, con, key, value: Mapping = None):
		super().__init__(con, key)
		if value is not None:
			if self.connection.hkeys(self.key):
				for k in self.connection.hkeys(self.key):
					self.connection.hdel(self.key, k)
			for k, v in value.items():
				self.connection.hset(self.key, k, self.encode(v))
		return
	
	def __repr__(self):
		_ = self.connection.hgetall(self.key)
		for k, v in _.items(): _[k] = self.decode(v)
		return _.__repr__()

	def __str__(self):
		_ = self.connection.hgetall(self.key)
		for k, v in _.items(): _[k] = self.decode(v)
		return _.__str__()
	
	def __getitem__(self, key):
		return self.decode(self.connection.hget(self.key, key))
	
	def __setitem__(self, key, value):
		return self.connection.hset(self.key, key, self.encode(value))
	
	def __delitem__(self, key):
		return self.connection.hdel(self.key, key)
	
	def __iter__(self):
		_ = self.connection.hgetall(self.key)
		return _.__iter__()
	
	def __len__(self):
		return self.connection.hlen(self.key)
	
	def __contains__(self, key):
		return self.connection.hexists(self.key, key)
	
	def __eq__(self, other):
		_ = self.connection.hgetall(self.key)
		for k, v in _.items(): _[k] = self.decode(v)
		return _.__eq__(other)
	
	def __ne__(self, value):
		_ = self.connection.hgetall(self.key)
		for k, v in _.items(): _[k] = self.decode(v)
		return _.__ne__(value)
	
	def keys(self):
		return self.connection.hkeys(self.key)

	def values(self):
		return self.connection.hvals(self.key)

	def items(self):
		_ = self.connection.hgetall(self.key)
		for k, v in _.items(): _[k] = self.decode(v)
		return _.items()
	