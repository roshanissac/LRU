# LRU
Least Recently Used Cache Implementation in Python

Here the LRU cache is implemented using OrderedDict.Unlike normal dictionary OrderedDict preserves the order and it tracks it when new items are inserted.We need to define the  maximum size of the cache and it should be positive integer. 

Below operations are supported,

### get(key)
Get the value (will always be positive) of the key if the key exists in the cache, otherwise KeyNotExistError exception will get triggered.

### put(key,value)
It will insert the value if the key is not already present.If the key exists it will trigger DuplicateKeyError exception.
When the cache reaches its maximum size,it will remove the least recently used item and adds the new item to the end of the dictionary.

### delete(key)
it will remove the item with the given key  if the key exists in the cache, otherwise there will be no operation.

### reset()
it will clear all the items from the cache.

## Running Examples 

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

