from lru import lruCache,KeyNotExistError,DuplicateKeyError,ValidSizeError

try:	
	cache=lruCache(3) # Setting the size of 3.Maximum 3 items can be added.
	cache.put(1,1)
	print(cache.cache)
	cache.put(2,2) # Adding second item 
	print(cache.cache)
	cache.put(3,3) # Adding third item 
	print(cache.cache)
	cache.get(1) # Accessing item with key 1,so the order will be [(2,2),(3,3),(1,1)]
	print(cache.cache)
	cache.put(4,4) # Adding fourth item ,since max size is 3 it will remove the least recently used item ie (2,2) and will add (4,4) to the end,so dict content be [(3,3),(1,1),(4,4)]
	print(cache.cache)
	cache.delete(1) # deleting the item with key 1 ,so dic content be [(3,3),(4,4)]
	print(cache.cache)
	cache.get(3) # Accessing item with key 3,so the order will be [(4,4),(3,3)],so element with key 3 will be most recently used and it is pushed to the end of the dictionary
	print(cache.cache)
	cache.put(5,5) # Adding 5th item ,it will be most recently used and pushed to the end [(4,4),(3,3),(5,5)]
	print(cache.cache)
	cache.reset() # Resetting the cache,All items is cleared
	print(cache.cache)
except ValidSizeError:
    print("Please enter a valid size")
except DuplicateKeyError:
    print("Key already exists,Please enter a new key!")
except KeyNotExistError:
    print("The key not exist or the cache is empty")