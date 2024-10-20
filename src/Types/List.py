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
				self.connection.rpush(self.key, v)
		return
	
	# implements interfaces of Sequence
	def __getitem__(self, index):
		return self.get(index)
	
	def __setitem__(self, index, value):
		return self.connection.lset(self.key, index, value)
	
	def __delitem__(self, index):
		return self.connection.lrem(self, index, self.connection.lrange(self.key, index, 1)[0])
	
	def __len__(self):
		return self.len()
	
	def __contains__(self, value):
		_ = self.connection.lrange(self.key, 0, -1)
		return _.__contains__(value)
	
	def __iter__(self):
		_ = self.connection.lrange(self.key, 0, -1)
		return _.__iter__()
	
	def __reversed__(self):
		_ = self.connection.lrange(self.key, 0, -1)
		return _.__reversed__()

	def __repr__(self):
		_ = self.connection.lrange(self.key, 0, -1)
		return _.__repr__()

	def __str__(self):
		_ = self.connection.lrange(self.key, 0, -1)
		return _.__str__()

	def count(self, value):
		_ = self.connection.lrange(self.key, 0, -1)
		return _.count(value)
	
	def insert(self, index, value):
		return self.connection.linsert(self.key, index, value, value)
	
	def append(self, value):
		return self.connection.rpush(self.key, value)
	
	def clear(self):
		return self.connection.lpop(self.key, self.connection.llen(self.key))
	
	def reverse(self):
		# TODO : 
		pass
	
	def extend(self, values):
		for v in values:
			self.connection.rpush(v)
		return
	
	def pop(self):
		return self.connection.lpop(self.key)
	
	def remove(self, value):
		return self.connection.lrem(self.key, 0, value)
	
	def __iadd__(self, values):
		for v in values if isinstance(values, Sequence) else [values]:
			self.connection.rpush(v)
		return
