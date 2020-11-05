from collections import OrderedDict

class ValidSize(Exception): 
    pass

class DuplicateKey(Exception): 
    pass

class KeyNotExist(Exception): 
    pass

class lruCache:
    def __init__(self, size: int):
        self.cache = OrderedDict()
        if isinstance(size,int) and size > 0:
        	self.size = size
        else:
            raise ValidSize


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            if len(self.cache) > self.size:
                self.cache.popitem(last = False)
        else:
            raise DuplicateKey


    def reset(self):
    	self.cache.clear()


    def delete(self, key: int) -> int:
        if key not in self.cache:
            raise KeyNotExist
        else:
            self.cache.pop(key)


#Initializing cache with max size

try:
    cache = lruCache(2)
    cache.put(1, 1)
    print(cache.cache)    
    cache.delete(2)
    print(cache.cache)
except ValidSize:
    print("Please enter a valid size")
except DuplicateKey:
    print("Key already exists,Please enter a new key!")
except KeyNotExist:
    print("The key not exist or the cache is empty")
