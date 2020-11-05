from collections import OrderedDict

class ValidCapacity(Exception): 
    pass

class lruCache:
    def __init__(self, size: int):
        self.cache = OrderedDict()
        if isinstance(size,int) and size > 0:
        	self.size = size
        else:
            raise ValidCapacity




#Initializing cache with max size

try:
    cache = lruCache(-2)
except ValidCapacity:
    print("Please enter a valid capacity")
