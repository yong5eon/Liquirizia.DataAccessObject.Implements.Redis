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
	con.set('sample:sample', json.dumps({
		1: 1,
		2: 2
	}))
	v = json.loads(con.get('sample:sample'))
	print(v, file=sys.stdout)
	# Set Persist
	con.persist('sample:sample')
	# Set Expires
	con.expire('sample:sample', 60)
	# Delete Value
	con.delete('sample:sample')

	# String Type
	stringType = String(con)
	stringType.set('sample:string', 'string')
	v = stringType.get('sample:string')
	print(v, file=sys.stdout)
	v = stringType.getSet('sample:string', 'changed')
	print(v, file=sys.stdout)
	v = stringType.get('sample:string')
	print(v, file=sys.stdout)
	v = stringType.len('sample:string')
	print(v, file=sys.stdout)
	con.delete('sample:string')

	# List Type
	listType = List(con)
	for i in range(0, 5):
		listType.push('sample:list', i)
		listType.push('sample:list', i)
	v = listType.get('sample:list')
	print(v, file=sys.stdout)
	con.delete('sample:list')

	# Set Type
	setType = Set(con)
	for i in range(0, 5):
		setType.add('sample:set', i)
		setType.add('sample:set', i)
	v = setType.get('sample:set')
	print(v, file=sys.stdout)
	con.delete('sample:set')

	# SortedSet Type
	sortedSetType = SortedSet(con)
	for i in range(0, 5):
		sortedSetType.add('sample:sortedSet', i, i)
		sortedSetType.add('sample:sortedSet', i, i)
	v = sortedSetType.get('sample:sortedSet')
	print(v, file=sys.stdout)
	con.delete('sample:sortedSet')

	# Hash Type
	hashType = Hash(con)
	for i in range(0, 5):
		hashType.set('sample:hash', i, i)
	v = hashType.getAll('sample:hash')
	print(v, file=sys.stdout)
	con.delete('sample:hash')
