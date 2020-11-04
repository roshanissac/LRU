from collections import OrderedDict

class lruCache:
    def __init__(self, size: int):
        self.cache = OrderedDict()
        self.size = size




#Initializing cache with max size
cache=lruCache(2)
print(cache.size)

