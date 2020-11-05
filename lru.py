from collections import OrderedDict

class ValidSizeError(Exception): 
    pass

class DuplicateKeyError(Exception): 
    pass

class KeyNotExistError(Exception): 
    pass

class lruCache:
    def __init__(self, size: int):
        self.cache = OrderedDict()
        if isinstance(size,int) and size > 0:
        	self.size = size
        else:
            raise ValidSizeError


    def put(self, key,value):

    	if key not in self.cache:
    		self.cache[key] = value
    		self.cache.move_to_end(key)
    		if len(self.cache) > self.size:
    			self.cache.popitem(last = False)
    	else:
        	raise DuplicateKeyError

    def get(self, key):
        if key not in self.cache:
            raise KeyNotExistError
        else:
            self.cache.move_to_end(key)
            return self.cache[key]


    def reset(self):
    	self.cache.clear()


    def delete(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.pop(key)



