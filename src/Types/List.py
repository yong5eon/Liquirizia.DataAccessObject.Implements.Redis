# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import MutableSequence, Sequence

__all__ = (
	'List'
)


class List(Type, MutableSequence):
	"""Type Helper Class for List"""

	def __init__(self, con, key, value: Sequence = None):
		super().__init__(con, key)
		if value is not None:
			if self.connection.llen(self.key):
				self.connection.lpop(self.key, self.connection.llen(self.key))
			for v in value:
				self.connection.rpush(self.key, self.encode(v))
		return
	
	# implements interfaces of Sequence
	def __getitem__(self, index):
		return self.decode(self.connection.lindex(self.key, index))
	
	def __setitem__(self, index, value):
		return self.connection.lset(self.key, index, self.encode(value))
	
	def __delitem__(self, index):
		return self.connection.lrem(self, index, self.connection.lrange(self.key, index, 1)[0])
	
	def __len__(self):
		return self.connection.llen(self.key)
	
	def __contains__(self, value):
		_ = self.connection.lrange(self.key, 0, -1)
		return _.__contains__(self.encode(value))
	
	def __iter__(self):
		_ = self.connection.lrange(self.key, 0, -1)
		for i, v in enumerate(_): _[i] = self.decode(v)
		return _.__iter__()
	
	def __reversed__(self):
		_ = self.connection.lrange(self.key, 0, -1)
		for i, v in enumerate(_): _[i] = self.decode(v)
		return _.__reversed__()

	def __repr__(self):
		_ = self.connection.lrange(self.key, 0, -1)
		for i, v in enumerate(_): _[i] = self.decode(v)
		return _.__repr__()

	def __str__(self):
		_ = self.connection.lrange(self.key, 0, -1)
		for i, v in enumerate(_): _[i] = self.decode(v)
		return _.__str__()

	def count(self, value):
		_ = self.connection.lrange(self.key, 0, -1)
		return _.count(self.encode(value))
	
	def insert(self, index, value):
		return self.connection.linsert(self.key, index, None, self.encode(value))
	
	def append(self, value):
		return self.connection.rpush(self.key, self.encode(value))
	
	def clear(self):
		return self.connection.lpop(self.key, self.connection.llen(self.key))
	
	def reverse(self):
		_ = self.connection.lrange(self.key, 0, -1)
		self.connection.lpop(self.key, self.connection.llen(self.key))
		_.reverse()
		for v in _:
				self.connection.rpush(self.key, _)
		return
	
	def extend(self, values):
		for v in values:
			self.connection.rpush(self.encode(v))
		return
	
	def pop(self):
		return self.decode(self.connection.lpop(self.key))
	
	def remove(self, value):
		return self.connection.lrem(self.key, 0, self.encode(value))
	
	def __iadd__(self, values):
		for v in values if isinstance(values, Sequence) else [values]:
			self.connection.rpush(self.encode(v))
		return
