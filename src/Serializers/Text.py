# -*- coding: utf-8 -*-

from ..Serializer import Serializer

from typing import Any

__all__ = (
	'Encoder',
	'Decoder',
)


class Encoder(Serializer):
	def __call__(self, v: Any):
		try:
			return str(v)
		except:
			return v

class Decoder(Serializer):
	def __call__(self, v):
		try:
			return eval(v)
		except:
			return v
	