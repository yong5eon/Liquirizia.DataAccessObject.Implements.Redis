# -*- coding: utf-8 -*-

from ..Serializer import Serializer

from json import loads, dumps
from typing import Any

__all__ = (
	'Encoder',
	'Decoder',
)


class Encoder(Serializer):
	def __call__(self, v: Any):
		try:
			return dumps(v)
		except:
			return v

class Decoder(Serializer):
	def __call__(self, v):
		try:
			return loads(v)
		except:
			return v
	