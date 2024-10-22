# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import MutableSet, Set, Sequence

__all__ = (
	'SortedSet'
)


class SortedSet(Type, MutableSet):
	"""Type Helper Class for Sorted Set"""

	def __init__(self, con, key, value: Set = None):
		super().__init__(con, key)
		if value is not None:
			if self.connection.zcard(self.key):
				for v in self.connection.zrange(self.key, 0, -1):
					self.connection.zrem(self.key, v)
			for v in value:
				if isinstance(v, Sequence):
					self.connection.zadd(self.key, {self.encode(v[0]): v[1]})
				else:
					self.connection.zadd(self.key, {self.encode(v): 0})
		return
	
	def __repr__(self):
		__ = set()
		_ = self.connection.zrange(self.key, 0, -1)
		for v in _: __.add(self.decode(v))
		__ = sorted(__)
		return __.__repr__()
	
	def __str__(self):
		__ = set()
		_ = self.connection.zrange(self.key, 0, -1)
		for v in _: __.add(self.decode(v))
		__ = sorted(__)
		return __.__str__()

	def __contains__(self, value):
		_ = self.connection.zrange(self.key, 0, -1)
		return value in _
	
	def __iter__(self):
		__ = set()
		_ = self.connection.zrange(self.key, 0, -1)
		for v in _: __.add(self.decode(v))
		__ = sorted(__)
		return __.__iter__()

	def __len__(self):
		return self.connection.zcard(self.key)
	
	def __le__(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__le__(other)
	
	def __lt__(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__lt__(other)
	
	def __eq__(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__eq__(other)
	
	def __ne__(self, value):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__ne__(value)
	
	def __gt__(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__gt__(self.encode(other))
	
	def __ge__(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__ge__(self.encode(other))
	
	def __and__(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__and__(self.encode(other))
	
	def __or__(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__or__(self.encode(other))
	
	def __sub__(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__sub__(self.encode(other))
	
	def __xor__(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__xor__(self.encode(other))
	
	def __iand__(self, it):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__iand__(self.encode(it))
	
	def __ior__(self, it):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__ior__(self.encode(it))
	
	def __ixor__(self, it):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__ixor__(self.encode(it))
	
	def __isub__(self, it):
		_ = self.connection.zrange(self.key, 0, -1)
		return _.__isub__(self.encode(it))
	
	def isdisjoint(self, other):
		_ = self.connection.zrange(self.key, 0, -1)
		# TODO : encode or decode
		return _.isdisjoint(other)
	
	def add(self, value, score=0, nx=False, xx=False, ch=False, incr=False):
		return self.connection.zadd(
			self.key, 
			{self.encode(value): score},
			nx=nx,
			xx=xx,
			ch=ch,
			incr=incr,
		)

	def discard(self, value):
		return self.connection.zrem(self.key, value)
	
	def clear(self):
		for v in self.connection.zrange(self.key, 0, -1):
			self.connection.zrem(self.key, v)
		return
	
	def pop(self):
		return self.connection.zrange(self.key, 0, 1)

	def remove(self, value):
		return self.connection.zrem(self.key, value)

	def score(self,value):
		return self.connection.zscore(self.key, value)
