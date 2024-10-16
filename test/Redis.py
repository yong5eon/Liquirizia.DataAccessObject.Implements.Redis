# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.DataAccessObject import Helper
from Liquirizia.DataAccessObject.Errors import *

from Liquirizia.DataAccessObject.Implements.Redis import Configuration, Connection
from Liquirizia.DataAccessObject.Implements.Redis.Types import *

from json import dumps, loads
from time import sleep
	

class Redis(Case):
	@classmethod
	def setUpClass(cls):
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
		return super().setUpClass()

	@Order(1)
	def testConnectClose(self):
		con = Helper.Get('Sample')
		ASSERT_IS_NOT_NONE(con)
		con.connect()
		con.close()
		return

	@Parameterized(
			{'k': 'sample', 'v': True},
			{'k': 'sample', 'v': 1},
			{'k': 'sample', 'v': 1.0},
			{'k': 'sample', 'v': "Hello"},
			# {'k': 'sample', 'v': (1,2,3)}, # TUPLE IS NOT SUPPORT
			{'k': 'sample', 'v': [1,2,3]},
			{'k': 'sample', 'v': {'a':1,'b':2}},
	)	
	@Order(2)
	def testSetGetDel(self, k, v):
		con = Helper.Get('Sample')
		# Get/Set Value
		if isinstance(v, (bool, int, float)):
			con.set(k, str(v))
			_ = eval(con.get(k))
			ASSERT_IS_EQUAL(v, _)
		elif isinstance(v, str):
			con.set(k, v)
			_ = con.get(k)
			ASSERT_IS_EQUAL(v, _)
		else:
			con.set(k, dumps(v))
			_ = loads(con.get(k))
			ASSERT_IS_EQUAL(v, _)
		con.delete(k)
		ASSERT_IS_NONE(con.get(k))
		return
	
	@Order(3)
	def testPersist(self):
		con = Helper.Get('Sample')
		con.set('sample', '1')
		con.expire('sample', 3)
		con.persist('sample')
		sleep(3)
		ASSERT_IS_NOT_NONE(con.get('sample'))	
		con.delete('sample')
		return

	@Order(4)
	def testExpire(self):
		con = Helper.Get('Sample')
		con.set('sample', '1')
		con.persist('sample')
		con.expire('sample', 3)
		sleep(3)
		ASSERT_IS_NONE(con.get('sample'))	
		con.delete('sample')
		return

	@Order(5)
	def testString(self):
		con = Helper.Get('Sample')
		stringType = String(con)
		stringType.set('sample', 'string')
		ASSERT_IS_EQUAL(stringType.get('sample'), 'string')
		ASSERT_IS_EQUAL(stringType.getSet('sample', 'changed'), 'string')
		ASSERT_IS_EQUAL(stringType.get('sample'), 'changed')
		ASSERT_IS_EQUAL(stringType.len('sample'), 7)
		con.delete('sample')
		return

	@Order(6)
	def testList(self):
		con = Helper.Get('Sample')
		listType = List(con)
		_ = []
		for i in range(0, 5):
			listType.push('sample', i)
			_.append(str(i))
		_.reverse()
		ASSERT_IS_EQUAL_LIST(listType.get('sample'), _)
		con.delete('sample')
		return

	@Order(7)
	def testSet(self):
		con = Helper.Get('Sample')
		setType = Set(con)
		_ = set()
		for i in range(0, 5):
			setType.add('sample', str(i))
			_.add(str(i))
		ASSERT_IS_EQUAL_SET(setType.get('sample'), _)
		con.delete('sample')
		return

	@Order(8)
	def testSortedSet(self):
		con = Helper.Get('Sample')
		sortedSetType = SortedSet(con)
		_ = []
		for i in range(0, 5):
			sortedSetType.add('sample', i, str(i))
			_.append(str(i))
		sorted(_)
		ASSERT_IS_EQUAL_LIST(sortedSetType.get('sample'), _)
		con.delete('sample')
		return

	@Order(9)
	def testHash(self):
		con = Helper.Get('Sample')
		hashType = Hash(con)
		_ = {}
		for i in range(0, 5):
			hashType.set('sample', i, str(i))
			_[str(i)] = str(i)
		ASSERT_IS_EQUAL_DICT(hashType.getAll('sample'), _)
		con.delete('sample')
		return

