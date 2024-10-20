# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Helper

from Liquirizia.DataAccessObject.Implements.Redis import Connection, Configuration

from Liquirizia.DataAccessObject.Implements.Redis.Types import String
from Liquirizia.DataAccessObject.Implements.Redis.Types import List
from Liquirizia.DataAccessObject.Implements.Redis.Types import Set
from Liquirizia.DataAccessObject.Implements.Redis.Types import SortedSet
from Liquirizia.DataAccessObject.Implements.Redis.Types import Hash

import sys
import json


if __name__ == '__main__':

	# Set connection
	Helper.Set(
		'Sample',
		Connection,
		Configuration(
			host='127.0.0.1',  # Redis Host Address
			port=6379,  # Redis Host Port
			max=1,  # Redis Maximum Connections
			persistent=True   # Is Persistent Connection
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

	# String Type
	stringType = String(con)
	stringType.set('sample', 'string')
	v = stringType.get('sample')
	print(v, file=sys.stdout)
	v = stringType.getSet('sample', 'changed')
	print(v, file=sys.stdout)
	v = stringType.get('sample')
	print(v, file=sys.stdout)
	v = stringType.len('sample')
	print(v, file=sys.stdout)
	con.delete('sample')

	# List Type
	listType = List(con)
	for i in range(0, 5):
		listType.push('sample', i)
		listType.push('sample', i)
	v = listType.get('sample')
	print(v, file=sys.stdout)
	con.delete('sample')

	# Set Type
	setType = Set(con)
	for i in range(0, 5):
		setType.add('sample', i)
		setType.add('sample', i)
	v = setType.get('sample')
	print(v, file=sys.stdout)
	con.delete('sample')

	# SortedSet Type
	sortedSetType = SortedSet(con)
	for i in range(0, 5):
		sortedSetType.add('sample', i, i)
		sortedSetType.add('sample', i, i)
	v = sortedSetType.get('sample')
	print(v, file=sys.stdout)
	con.delete('sample')

	# Hash Type
	hashType = Hash(con)
	for i in range(0, 5):
		hashType.set('sample', i, i)
	v = hashType.getAll('sample')
	print(v, file=sys.stdout)
	con.delete('sample')
