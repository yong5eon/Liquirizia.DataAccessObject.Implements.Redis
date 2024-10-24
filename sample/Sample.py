# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Helper

from Liquirizia.DataAccessObject.Implements.Redis import (
	Connection,
	Configuration,
	ConnectionType,
)

from random import randint
import sys

if __name__ == '__main__':

	# Set connection
	Helper.Set(
		'Sample',
		Connection,
		Configuration(
			host='127.0.0.1',  # Redis Host Address
			port=6379,  # Redis Host Porta
		)
	)

	# Get Connection
	con = Helper.Get('Sample')

	# Get/Set Value
	_ = [
		True, # boolean
		False,
		0, # integer
		0.0, # float
		'string', # string
		(1,2,3), # tuple
		[1,2,3], # list
		set([1,2,3]), # set
		{1:1,2:2,3:3}, # dict
	]
	for v in _:
		con.set('sample', v)
		print(con.get('sample'), file=sys.stdout)

	## Set Persist
	con.persist('sample')
	## Set Expires
	con.expire('sample', 60)
	## Delete Value
	con.delete('sample')

	# List Type
	_ = con.setList('sample', [0,1,2,3,4])
	print(_, file=sys.stdout)
	_ = con.getList('sample')
	print(_, file=sys.stdout)
	_ = con.setList('sample')
	print(_, file=sys.stdout)
	for i in range(0, 5):
		_.append(randint(i, i*5))
	print(_, file=sys.stdout)
	_ = con.getList('sample')
	print(_, file=sys.stdout)
	for v in _:
		print(v, file=sys.stdout)
	con.delete('sample')

	# Set Type
	_ = con.setSet('sample', {0,1,2,3,4})
	print(_, file=sys.stdout)
	_ = con.getSet('sample')
	print(_, file=sys.stdout)
	_ = con.setSet('sample')
	print(_, file=sys.stdout)
	for i in range(0, 5):
		_.add(randint(i, i*5))
	print(_, file=sys.stdout)
	_ = con.getSet('sample')
	print(_, file=sys.stdout)
	for v in _:
		print(v, file=sys.stdout)
	con.delete('sample')

	# SortedSet Type
	_ = con.setSortedSet('sample', {0,1,4,2,3})
	print(_, file=sys.stdout)
	_ = con.getSortedSet('sample')
	print(_, file=sys.stdout)
	_ = con.setSortedSet('sample')
	print(_, file=sys.stdout)
	for i in range(0, 5):
		_.add(randint(i, i*5))
	print(_, file=sys.stdout)
	_ = con.getSortedSet('sample')
	print(_, file=sys.stdout)
	for v in _:
		print(v, file=sys.stdout)
	con.delete('sample')

	# Hash Type
	__ = {
		'a': True,
		'b': 1,
		'c': 0.0,
		'd': (1,2,3),
		'e': [1,2,3],
		'f': {'a': False, 'b': 0, 'c': 1.0},
	}
	_ = con.setHash('sample', __)
	print(_, file=sys.stdout)
	_ = con.getHash('sample')
	print(_, file=sys.stdout)
	_ = con.setHash('sample')
	print(_, file=sys.stdout)
	for k, v in __.items():
		_[k] = v
	print(_, file=sys.stdout)
	_ = con.getHash('sample')
	print(_, file=sys.stdout)
	for k, v in _.items():
		print(k, v, file=sys.stdout)
	con.delete('sample')
