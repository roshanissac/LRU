# LRU
Least Recently Used Cache Implementation in Python

Here the LRU cache is implemented using OrderedDict.Unlike normal dictionary OrderedDict preserves the order and it tracks it when new items are inserted.We need to define the  maximum size of the cache and it should be positive integer. 

All the operations has a time complexity of O(1). The OrderedDict is maintained in a such way that in the beginning we will have the least recently used item and in the end ,most recently used.

Any get(key) or put(key,value) operations made to the key will moves it to the end(most recently used.)

Below operations are supported,

### get(key)
Get the value (will always be positive) of the key if the key exists in the cache, otherwise KeyNotExistError exception will get triggered.

### put(key,value)
It will insert the value if the key is not already present.If the key exists it will trigger DuplicateKeyError exception.
When the cache reaches its maximum size,it will remove the least recently used item and adds the new item to the end of the dictionary.

### delete(key)
it will remove the item with the given key if the key exists in the cache, otherwise there will be no operation.

### reset()
it will clear all the items from the cache.

## Examples 

### importing classes

lru.py is the base file and on the new file which implement the logic(eg.sample.py) we need to import the required classes like below,

```
from lru import lruCache,KeyNotExistError,DuplicateKeyError,ValidSizeError

```

### setting the max size of the cache

It will create a cache with maximun size 2.
```
cache=lruCache(2)

```
### Inserting a new element into the cache

Below will insert key 1 with value 1,each item will be in (key,value) pair.
```
cache.put(1,1)

```
### Accessing an existing element in the cache

Get the value with key 1 from the cache.
```
cache.get(1)

```
### Delete an element in the cache

Delete the item with key 1.
```
cache.delete(1)

```
### Reset the cache

It will clear the cache.
```
cache.reset()

```
### Handling Exceptions 

Here we are trying to create a cache by passing a negative value as its size.It will trigger ValidSizeError exception and can be handled like below.
```
try:
    cache = lruCache(-2)
except ValidSizeError:
    print("Please enter a valid size")
except DuplicateKeyError:
    print("Key already exists,Please enter a new key!")
except KeyNotExistError:
    print("The key not exist or the cache is empty")

```
Above outputs

```
Please enter a valid size
```
### Fullworking Example

A full working example is given in the file sample.py and can be executed in python like below,

```
python sample.py
```
and it outputs
```
OrderedDict([(1,1)])
OrderedDict([(1, 1), (2, 2)])
OrderedDict([(1, 1), (2, 2), (3, 3)])
OrderedDict([(2, 2), (3, 3), (1, 1)])
OrderedDict([(3, 3), (1, 1), (4, 4)])
OrderedDict([(3, 3), (4, 4)])
OrderedDict([(4, 4), (3, 3)])
OrderedDict([(4, 4), (3, 3), (5, 5)])
OrderedDict()
```

## Executing Unit Tests

I have used unittest unit testing framework to execute test cases. The file unit_test_cases.py consists of the test cases and it can be run from the terminal/command prompt like below.
```
python unit_test_cases.py
```
or
```
python -m unittest unit_test_cases.py
```
or
```
python -m unittest unit_test_cases.MyTestCase
```
Also even we can execute each unit cases separately like,
```
python -m unittest unit_test_cases.MyTestCase.test_1
```

