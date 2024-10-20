# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Helper

from Liquirizia.DataAccessObject.Implements.Redis import Connection, Configuration

from Liquirizia.DataAccessObject.Implements.Redis.Types import List
from Liquirizia.DataAccessObject.Implements.Redis.Types import Set
from Liquirizia.DataAccessObject.Implements.Redis.Types import SortedSet
from Liquirizia.DataAccessObject.Implements.Redis.Types import Hash

from random import randint

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
	con.set('sample', json.dumps({
		1: 1,
		2: 2
	}))
	v = json.loads(con.get('sample'))
	print(v, file=sys.stdout)
	# Set Persist
	con.persist('sample')
	# Set Expires
	con.expire('sample', 60)
	# Delete Value
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
	con.delete('sample')

	# # Set Type
	# setType = Set(con)
	# for i in range(0, 5):
	# 	setType.add('sample:set', i)
	# 	setType.add('sample:set', i)
	# v = setType.get('sample:set')
	# print(v, file=sys.stdout)
	# con.delete('sample:set')

	# # SortedSet Type
	# sortedSetType = SortedSet(con)
	# for i in range(0, 5):
	# 	sortedSetType.add('sample:sortedSet', i, i)
	# 	sortedSetType.add('sample:sortedSet', i, i)
	# v = sortedSetType.get('sample:sortedSet')
	# print(v, file=sys.stdout)
	# con.delete('sample:sortedSet')

	# # Hash Type
	# hashType = Hash(con)
	# for i in range(0, 5):
	# 	hashType.set('sample:hash', i, i)
	# v = hashType.getAll('sample:hash')
	# print(v, file=sys.stdout)
	# con.delete('sample:hash')
