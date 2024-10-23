# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Configuration as BaseConfiguration

from .Serializer import Serializer
from .Serializers.Text import (
	Encoder as Encoder,
	Decoder as Decoder,
)

from enum import Enum, auto

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
		host: str,
		port: int = 6379,
		username: str = None,
		password: str = None,
		type: ConnectionType = None,
		max: int = 3,
		encoder: Serializer = Encoder(),
		decoder: Serializer = Decoder(),
	):
		self.host = host
		self.port = port
		self.user = username
		self.password = password
		self.type = type
		self.max = max
		self.encoder = encoder
		self.decoder = decoder
		return
