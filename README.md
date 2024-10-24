# Liquirizia.DataAccessObject.Implements.Redis

Redis Data Access Object for Liquirizia

## 사용 방법

```python
from Liquirizia.DataAccessObject import DataAccessObjectHelper  # 데이터 접근 헬퍼 임포트

from Liquirizia.DataAccessObject.Implements.Redis import DataAccessObject, DataAccessObjectConfiguration  # 레디스 접근 객체 임포트

import sys
import json

if __name__ == '__main__':

  # Set connection
  DataAccessObjectHelper.Set(
    'Sample',
    DataAccessObject,
    DataAccessObjectConfiguration(
      host='YOUR_HOST',  # Redis Host Address, String
      port=YOUR_PORT,  # Redis Host Port, Integer
      max=YOUR_MAX_CONNECTION,  # Redis Maximum Connections, Integer
      persistent=YOUR_PERSISTENT_CONNECTION_SETTING   # Is Persistent Connection, Boolean(True/False)
    )
  )

  # Get Connection
  con = DataAccessObjectHelper.Get('Sample')

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
```

## 데이터 타입 별 접근 방법

### 문자열 데이터 타입 접근

```python
from Liquirizia.DataAccessObject import DataAccessObjectHelper  # 데이터 접근 헬퍼 임포트

from Liquirizia.DataAccessObject.Implements.Redis import DataAccessObject, DataAccessObjectConfiguration  # 레디스 접근 객체 임포트
from Liquirizia.DataAccessObject.Implements.Redis.Types import DataStringObject

import sys

if __name__ == '__main__':

  # Set connection
  DataAccessObjectHelper.Set(
    'Sample',
    DataAccessObject,
    DataAccessObjectConfiguration(
      host='YOUR_HOST',  # Redis Host Address, String
      port=YOUR_PORT,  # Redis Host Port, Integer
      max=YOUR_MAX_CONNECTION,  # Redis Maximum Connections, Integer
      persistent=YOUR_PERSISTENT_CONNECTION_SETTING   # Is Persistent Connection, Boolean(True/False)
    )
  )

  # Get Connection
  con = DataAccessObjectHelper.Get('Sample')

  # String Type
  stringType = DataStringObject(con)
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
```

### 리스트 데이터 타입 접근

```python
from Liquirizia.DataAccessObject import DataAccessObjectHelper  # 데이터 접근 헬퍼 임포트

from Liquirizia.DataAccessObject.Implements.Redis import DataAccessObject, DataAccessObjectConfiguration  # 레디스 접근 객체 임포트
from Liquirizia.DataAccessObject.Implements.Redis.Types import DataListObject

import sys

if __name__ == '__main__':

  # Set connection
  DataAccessObjectHelper.Set(
    'Sample',
    DataAccessObject,
    DataAccessObjectConfiguration(
      host='YOUR_HOST',  # Redis Host Address, String
      port=YOUR_PORT,  # Redis Host Port, Integer
      max=YOUR_MAX_CONNECTION,  # Redis Maximum Connections, Integer
      persistent=YOUR_PERSISTENT_CONNECTION_SETTING   # Is Persistent Connection, Boolean(True/False)
    )
  )

  # Get Connection
  con = DataAccessObjectHelper.Get('Sample')
  
  # List Type
  listType = DataListObject(con)
  for i in range(0, 5):
    listType.push('sample:list', i)
    listType.push('sample:list', i)
  v = listType.get('sample:list')
  print(v, file=sys.stdout)
  con.delete('sample:list')
```  

### 세트 데이터 타입 접근

```python
from Liquirizia.DataAccessObject import DataAccessObjectHelper  # 데이터 접근 헬퍼 임포트

from Liquirizia.DataAccessObject.Implements.Redis import DataAccessObject, DataAccessObjectConfiguration  # 레디스 접근 객체 임포트
from Liquirizia.DataAccessObject.Implements.Redis.Types import DataSetObject

import sys

if __name__ == '__main__':

  # Set connection
  DataAccessObjectHelper.Set(
    'Sample',
    DataAccessObject,
    DataAccessObjectConfiguration(
      host='YOUR_HOST',  # Redis Host Address, String
      port=YOUR_PORT,  # Redis Host Port, Integer
      max=YOUR_MAX_CONNECTION,  # Redis Maximum Connections, Integer
      persistent=YOUR_PERSISTENT_CONNECTION_SETTING   # Is Persistent Connection, Boolean(True/False)
    )
  )

  # Get Connection
  con = DataAccessObjectHelper.Get('Sample')
  
  # Set Type
  setType = DataSetObject(con)
  for i in range(0, 5):
    setType.add('sample:set', i)
    setType.add('sample:set', i)
  v = setType.get('sample:set')
  print(v, file=sys.stdout)
  con.delete('sample:set')
```

### 정렬된 세트 데이터 타입 접근

```python
from Liquirizia.DataAccessObject import DataAccessObjectHelper  # 데이터 접근 헬퍼 임포트

from Liquirizia.DataAccessObject.Implements.Redis import DataAccessObject, DataAccessObjectConfiguration  # 레디스 접근 객체 임포트
from Liquirizia.DataAccessObject.Implements.Redis.Types import DataSortedSetObject

import sys

if __name__ == '__main__':
  
  # Set connection
  DataAccessObjectHelper.Set(
    'Sample',
    DataAccessObject,
    DataAccessObjectConfiguration(
      host='YOUR_HOST',  # Redis Host Address, String
      port=YOUR_PORT,  # Redis Host Port, Integer
      max=YOUR_MAX_CONNECTION,  # Redis Maximum Connections, Integer
      persistent=YOUR_PERSISTENT_CONNECTION_SETTING   # Is Persistent Connection, Boolean(True/False)
    )
  )

  # Get Connection
  con = DataAccessObjectHelper.Get('Sample')
  
  # SortedSet Type
  sortedSetType = DataSortedSetObject(con)
  for i in range(0, 5):
    sortedSetType.add('sample:sortedSet', i, i)
    sortedSetType.add('sample:sortedSet', i, i)
  v = sortedSetType.get('sample:sortedSet')
  print(v, file=sys.stdout)
  con.delete('sample:sortedSet')
```

### 해시 데이터 타입 접근

```python
from Liquirizia.DataAccessObject import DataAccessObjectHelper  # 데이터 접근 헬퍼 임포트

from Liquirizia.DataAccessObject.Implements.Redis import DataAccessObject, DataAccessObjectConfiguration  # 레디스 접근 객체 임포트
from Liquirizia.DataAccessObject.Implements.Redis.Types import DataHashObject

import sys

if __name__ == '__main__':
  
  # Set connection
  DataAccessObjectHelper.Set(
    'Sample',
    DataAccessObject,
    DataAccessObjectConfiguration(
      host='YOUR_HOST',  # Redis Host Address, String
      port=YOUR_PORT,  # Redis Host Port, Integer
      max=YOUR_MAX_CONNECTION,  # Redis Maximum Connections, Integer
      persistent=YOUR_PERSISTENT_CONNECTION_SETTING   # Is Persistent Connection, Boolean(True/False)
    )
  )

  # Get Connection
  con = DataAccessObjectHelper.Get('Sample')
  
  # Hash Type
  hashType = DataHashObject(con)
  for i in range(0, 5):
    hashType.set('sample:hash', i, i)
  v = hashType.getAll('sample:hash')
  print(v, file=sys.stdout)
  con.delete('sample:hash')

```

## 도커 빌드 및 실행

### Redis

```shell
> docker image build --file=res/Redis.7.docker.yml --tag=redis:7 .
> docker container run --name=redis --detach --publish=6379:6379 redis:7
```

### Redis Cluster

```shell
> docker image build --file=res/Redis.7.docker.yml --tag=redis:7 .
> docker-compose -p redis-cluster -f res/Redis.7.Cluster.docker-compose.yml up -d
```
