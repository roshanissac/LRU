from collections import OrderedDict

class lruCache:
    def __init__(self, size: int):
        self.cache = OrderedDict()
        self.size = size




#Initializing cache with max size
cache=lruCache(3)
print(cache.size)

