# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.DataAccessObject import Helper
from Liquirizia.DataAccessObject.Errors import *

from Liquirizia.DataAccessObject.Implements.Redis import Configuration, Connection
from Liquirizia.DataAccessObject.Implements.Redis.Types import *

from json import dumps, loads
from time import sleep
from random import randint
	

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
			{'k': 'sample', 'v': False},
			{'k': 'sample', 'v': 1},
			{'k': 'sample', 'v': 1.0},
			{'k': 'sample', 'v': "Hello"},
			{'k': 'sample', 'v': (1,2,3)}, 
			{'k': 'sample', 'v': [1,2,3]},
			{'k': 'sample', 'v': {1,2,3}},
			{'k': 'sample', 'v': {'a':1,'b':2}},
	)	
	@Order(2)
	def testSetGetDel(self, k, v):
		con = Helper.Get('Sample')
		# Get/Set Value
		con.set(k, v)
		_ = con.get(k)
		ASSERT_IS_EQUAL(v, _)
		con.delete(k)
		ASSERT_IS_NONE(con.get(k))
		return
	
	@Order(3)
	def testPersist(self):
		con = Helper.Get('Sample')
		con.set('sample', 1)
		con.expire('sample', 3)
		con.persist('sample')
		sleep(5)
		ASSERT_IS_NOT_NONE(con.get('sample'))	
		con.delete('sample')
		return

	@Order(4)
	def testExpire(self):
		con = Helper.Get('Sample')
		con.set('sample', 1)
		con.persist('sample')
		con.expire('sample', 3)
		sleep(5)
		ASSERT_IS_NONE(con.get('sample'))	
		con.delete('sample')
		return

	@Order(5)
	def testList(self):
		con = Helper.Get('Sample')
		v = [True, 1, 2, 4.0, 6.0, 'ABC', False]
		_ = con.setList('sample', v)
		ASSERT_IS_EQUAL_SEQUENCE(_, v)
		_ = con.getList('sample')
		ASSERT_IS_EQUAL_SEQUENCE(_, v)
		_ = con.setList('sample')
		v = []
		for i in range(0, 5):
			x = randint(i+1, (i+1)*100)
			_.append(x)
			v.append(x)
		ASSERT_IS_EQUAL_SEQUENCE(_, v)
		for i, __ in enumerate(_):
			ASSERT_IS_EQUAL(_[i], v[i])
		con.delete('sample')
		return

	@Order(6)
	def testSet(self):
		con = Helper.Get('Sample')
		v = set()
		for i in range(0, 10):
			x = randint(i+1, (i+1)*100)
			v.add(x)
		_ = sorted(con.setSet('sample', v))
		ASSERT_IS_EQUAL_SEQUENCE(_, sorted(v))
		_ = sorted(con.getSet('sample'))
		ASSERT_IS_EQUAL_SEQUENCE(_, sorted(v))
		_ = con.setSet('sample')
		v = set()
		for i in range(0, 10):
			x = randint(i+1, (i+1)*100)
			v.add(x)
			_.add(x)
		_ = sorted(con.getSet('sample'))
		ASSERT_IS_EQUAL_SEQUENCE(_, sorted(v))
		con.delete('sample')
		return

	@Order(7)
	def testSortedSet(self):
		con = Helper.Get('Sample')
		v = set()
		for i in range(0, 10):
			x = randint(i+1, (i+1)*100)
			v.add(x)
		_ = sorted(con.setSortedSet('sample', v))
		ASSERT_IS_EQUAL_SEQUENCE(_, sorted(v))
		_ = sorted(con.getSortedSet('sample'))
		ASSERT_IS_EQUAL_SEQUENCE(_, sorted(v))
		_ = con.setSortedSet('sample')
		v = set()
		for i in range(0, 10):
			x = randint(i+1, (i+1)*100)
			v.add(x)
			_.add(x)
		_ = sorted(con.getSortedSet('sample'))
		ASSERT_IS_EQUAL_SEQUENCE(_, sorted(v))
		con.delete('sample')
		return

	@Order(8)
	def testHash(self):
		from copy import deepcopy
		con = Helper.Get('Sample')
		v = {
			'a': True,
			'b': 1,
			'c': 0.0,
			'd': (1,2,3),
			'e': [1,2,3],
			'f': {'a': False, 'b': 0, 'c': 1.0},
		}
		_ = con.setHash('sample', v)
		ASSERT_IS_EQUAL_DICT(deepcopy(_), v)
		_ = con.getHash('sample')
		ASSERT_IS_EQUAL_DICT(deepcopy(_), v)
		_ = con.setHash('sample')
		for k, va in v.items():
			_[k] = va
		_ = con.getHash('sample')
		ASSERT_IS_EQUAL_DICT(deepcopy(_), v)
		con.delete('sample')