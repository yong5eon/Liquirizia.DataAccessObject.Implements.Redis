# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from typing import Any

__all__ = (
	'Serializer'
)


class Serializer(metaclass=ABCMeta):
	"""Abstract Serializer Class for Redis"""

	@abstractmethod
	def __call__(self, v: Any):
		pass
