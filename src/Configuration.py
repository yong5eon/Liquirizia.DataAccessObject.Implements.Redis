# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Configuration as BaseConfiguration

from .Serializer import Serializer
from .Serializers.Text import (
	Encoder as Encoder,
	Decoder as Decoder,
)

from enum import Enum, auto
from typing import Sequence, Union

__all__ = (
	'Configuration',
	'ConnectionType',
)


class ConnectionType(Enum):
	Pool = auto()
	Cluster = auto()


class Configuration(BaseConfiguration):
	"""Configuration Class for Redis"""

	def __init__(
		self,
		host: str = None,
		port: int = 6379,
		username: str = None,
		password: str = None,
		secure: bool = False,
		type: ConnectionType = None,
		max: int = 1,
		encoder: Serializer = Encoder(),
		decoder: Serializer = Decoder(),
	):
		self.host = host
		self.port = port
		self.username = username
		self.password = password
		self.secure = secure
		self.type = type
		self.max = max
		self.encoder = encoder
		self.decoder = decoder
		self.database = 0
		self.url = 'rediss://' if self.secure else 'redis://'
		if self.username:
			self.url += self.username
			if self.password:
				self.url += ':' + self.password
			self.url += '@'
		self.url += '{}:{}/{}'.format(self.host, self.port, self.database)
		return
