# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Configuration as BaseConfiguration

from .Serializer import Serializer
from .Serializers.Text import (
	Encoder as Encoder,
	Decoder as Decoder,
)

__all__ = (
	'Configuration'
)


class Configuration(BaseConfiguration):
	"""Configuration Class for Redis"""

	def __init__(
		self,
		host,
		port=6379,
		username=None,
		password=None,
		max=3,
		persistent=True,
		encoder: Serializer = Encoder(),
		decoder: Serializer = Decoder(),
	):
		self.host = host
		self.port = port
		self.user = username
		self.password = password
		self.max = max
		self.persist = persistent
		self.encoder = encoder
		self.decoder = decoder
		return
