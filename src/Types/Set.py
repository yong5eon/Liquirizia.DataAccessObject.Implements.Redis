# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import MutableSet, Set

__all__ = (
	'Set'
)


class Set(Type, MutableSet):
	"""Type Helper Class for Set"""

	def __init__(self, con, key, value: Set = None):
		super().__init__(con, key)
		if value is not None:
			if self.connection.scard(self.key):
				self.connection.spop(self.key, self.connection.scard(self.key))
			for v in value:
				self.connection.sadd(self.key, self.encode(v))
		return
	
	def __repr__(self):
		_ = list(self.connection.smembers(self.key))
		for i, v in enumerate(_): _[i] = self.decode(v)
		return _.__repr__()
	
	def __str__(self):
		_ = list(self.connection.smembers(self.key))
		for i, v in enumerate(_): _[i] = self.decode(v)
		_ = set(_)
		return _.__str__()

	def __contains__(self, value):
		return self.connection.sismember(self.key, self.encode(value))
	
	def __iter__(self):
		_ = list(self.connection.smembers(self.key))
		for i, v in enumerate(_): _[i] = self.decode(v)
		_ = set(_)
		return _.__iter__()
	
	def __len__(self):
		return self.connection.scard(self.key)
	
	def __le__(self, other):
		_ = self.connection.smembers(self.key)
		return _.__le__(other)
	
	def __lt__(self, other):
		_ = self.connection.smembers(self.key)
		return _.__lt__(other)
	
	def __eq__(self, other):
		_ = self.connection.smembers(self.key)
		return _.__eq__(other)
	
	def __ne__(self, value):
		_ = self.connection.smembers(self.key)
		return _.__ne__(value)
	
	def __gt__(self, other):
		_ = self.connection.smembers(self.key)
		return _.__gt__(self.encode(other))
	
	def __ge__(self, other):
		_ = self.connection.smembers(self.key)
		return _.__ge__(self.encode(other))
	
	def __and__(self, other):
		_ = self.connection.smembers(self.key)
		return _.__and__(self.encode(other))
	
	def __or__(self, other):
		_ = self.connection.smembers(self.key)
		return _.__or__(self.encode(other))
	
	def __sub__(self, other):
		_ = self.connection.smembers(self.key)
		return _.__sub__(self.encode(other))
	
	def __xor__(self, other):
		_ = self.connection.smembers(self.key)
		return _.__xor__(self.encode(other))
	
	def __iand__(self, it):
		_ = self.connection.smembers(self.key)
		return _.__iand__(self.encode(it))
	
	def __ior__(self, it):
		_ = self.connection.smembers(self.key)
		return _.__ior__(self.encode(it))
	
	def __ixor__(self, it):
		_ = self.connection.smembers(self.key)
		return _.__ixor__(self.encode(it))
	
	def __isub__(self, it):
		_ = self.connection.smembers(self.key)
		return _.__isub__(self.encode(it))
	
	def isdisjoint(self, other):
		_ = self.connection.smembers(self.key)
		# TODO : encode or decode
		return _.isdisjoint(other)
	
	def add(self, value):
		return self.connection.sadd(self.key, self.encode(value))

	def discard(self, value):
		return self.connection.srem(self.key, value)
	
	def clear(self):
		return self.connection.spop(self.key, self.connection.scard(self.key))
	
	def pop(self):
		return self.connection.spop(self.key)

	def remove(self, value):
		return self.connection.srem(self.key, value)
