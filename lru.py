
#importing OrderedDic from collections module
from collections import OrderedDict

#Classes for handling exceptions
class ValidSizeError(Exception): 
    pass

class DuplicateKeyError(Exception): 
    pass

class KeyNotExistError(Exception): 
    pass

#main class for the lru logic
class lruCache:
    def __init__(self, size: int):
        self.cache = OrderedDict() # Initializing an ordered dictionary
        if isinstance(size,int) and size > 0:
        	self.size = size # setting the size of the cache
        else:
            raise ValidSizeError # raising error if invalid value for the size variable

'''put method is will get the key and value to be inserted and it will move the new item to the end of the dictionary and if the size of the cache 
exceeds the maximum size it will remove the least recently used item,which will be the first element of the dictionary.If we are inserting a duplicate key
then DuplicateKeyError exception is raised.
'''
    def put(self, key,value):

    	if key not in self.cache:
    		self.cache[key] = value
    		self.cache.move_to_end(key)
    		if len(self.cache) > self.size:
    			self.cache.popitem(last = False)
    	else:
        	raise DuplicateKeyError
'''get method will return the value of the key passed and it also moves that item to the end of the dictionary as it was recently used.If the key passed doesnt
exist in the dictionary it will raise KeyNotExistError exception

'''
    def get(self, key):
        if key not in self.cache:
            raise KeyNotExistError
        else:
            self.cache.move_to_end(key)
            return self.cache[key]


    def reset(self):
    	self.cache.clear()#clears the items from the dictionary


    def delete(self, key):
        if key not in self.cache:# No operation if the key not found
            return -1
        else:
            self.cache.pop(key)# removes the key found 



