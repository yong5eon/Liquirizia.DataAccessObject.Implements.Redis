# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Type as BaseType

from .Connection import Connection

__all__ = (
	'Type'
)


class Type(BaseType):
	"""Abstract Type Class for Redis"""

	def __init__(self, con: Connection, key: str):
		self.connection = con.connection
		self.key = key
		return
