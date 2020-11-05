import unittest
from collections import OrderedDict
from lru import lruCache,KeyNotExistError,DuplicateKeyError,ValidSizeError

'''
try:
    cache = lruCache(2)
    cache.put(1, 1)
    print(cache.cache)    
    cache.get(2)
    print(cache.cache)
except ValidSize:
    print("Please enter a valid size")
except DuplicateKey:
    print("Key already exists,Please enter a new key!")
except KeyNotExist:
    print("The key not exist or the cache is empty")
'''
class MyTestCase(unittest.TestCase): 
  
   # Returns true if lruCache(-2) raises a ValidSizeError 
   def test_1(self): 
      with self.assertRaises(Exception):
      	lruCache(-2) # Passing negative value as the size of the cache

   # Returns true if lruCache(0) raises a ValidSizeError 
   def test_2(self): 
      with self.assertRaises(Exception): 
        lruCache(0) # Passing zero value as the size of the cache

   # Returns true if lruCache('skjhdf') raises a ValidSizeError 
   def test_3(self): 
      with self.assertRaises(Exception): 
        lruCache('skjhdf') # Passing string as the size of the cache

    # Returns true if lruCache(5.67) raises a ValidSizeError 
   def test_4(self): 
      with self.assertRaises(Exception): 
        lruCache(5.67) # Passing float value as the size of the cache

   # # Returns true if it raises a KeyNotExistError 
   # def test_5(self): 
   #    with self.assertRaises(Exception): 
   #      cache=lruCache(2) # Setting the size 
   #      cache.delete(1) # deleting an item without even adding it

   # # Returns true if it raises a KeyNotExistError 
   # def test_6(self): 
   #    with self.assertRaises(Exception): 
   #      cache=lruCache(2) # Setting the size 
   #      cache.put(1,1)
   #      cache.delete(2) # deleting key that doesnt exist

   # Returns true if it raises a DuplicateKeyError 
   def test_5(self): 
      with self.assertRaises(Exception): 
        cache=lruCache(2) # Setting the size 
        cache.put(1,1)
        cache.put(1,1) # Adding again an item with the same key

   # The test will pass if both dictionaries has the same elements in correct order,latest added will will go to end 
   def test_6(self):
   	cache=lruCache(2) # Setting the size 
   	cache.put(1,1)
   	cache.put(2,1) # Adding second item 
   	self.result=cache.cache
   	self.expected=OrderedDict([(1,1),(2,1)])
   	self.assertDictEqual(self.result,self.expected)


   # The test will pass if both dictionaries has the same elements in correct order,recently accessed item will will go to end 
   def test_7(self):
   	cache=lruCache(2) # Setting the size 
   	cache.put(1,1)
   	cache.put(2,1) # Adding second item 
   	cache.get(1) # Accessing item with key 1
   	self.result=cache.cache
   	self.expected=OrderedDict([(2,1),(1,1)]) # key 1 will get moved to the end since it is recently used
   	self.assertDictEqual(self.result,self.expected)

    # The test will pass if both dictionaries has the same elements in correct order,recently accessed/added item will will go to end 
   def test_8(self):
   	cache=lruCache(3) # Setting the size 
   	cache.put(1,1)
   	cache.put(2,2) # Adding second item 
   	cache.put(3,3) # Adding third item 
   	cache.get(1) # Accessing item with key 1,so the order will be [(2,2),(3,3),(1,1)]
   	cache.put(4,4) # Adding fourth item ,since max size is 3 it will remove the least recently used item ie (2,2) and will add (4,4) to the end,so dict content be [(3,3),(1,1),(4,4)]
   	self.result=cache.cache
   	self.expected=OrderedDict([(3,3),(1,1),(4,4)]) 
   	self.assertDictEqual(self.result,self.expected)

   	# The test will pass if both dictionaries has the same elements in correct order,recently accessed item will will go to end 
   def test_9(self):
   	cache=lruCache(3) # Setting the size 
   	cache.put(1,1)
   	cache.put(2,2) # Adding second item 
   	cache.put(3,3) # Adding third item 
   	cache.get(1) # Accessing item with key 1,so the order will be [(2,2),(3,3),(1,1)]
   	cache.put(4,4) # Adding fourth item ,since max size is 3 it will remove the least recently used item ie (2,2) and will add (4,4) to the end,so dict content be [(3,3),(1,1),(4,4)]
   	cache.delete(1) # deleting the item with key 1 ,so dic content be [(3,3),(4,4)]
   	self.result=cache.cache
   	self.expected=OrderedDict([(3,3),(4,4)]) 
   	self.assertDictEqual(self.result,self.expected)

   	# The test will pass if both dictionaries has the same elements in correct order,recently accessed item will will go to end 
   def test_10(self):
   	cache=lruCache(3) # Setting the size 
   	cache.put(1,1)
   	cache.put(2,2) # Adding second item 
   	cache.put(3,3) # Adding third item 
   	cache.get(1) # Accessing item with key 1,so the order will be [(2,2),(3,3),(1,1)]
   	cache.put(4,4) # Adding fourth item ,since max size is 3 it will remove the least recently used item ie (2,2) and will add (4,4) to the end,so dict content be [(3,3),(1,1),(4,4)]
   	cache.delete(5) # Attempting to delete a key that doesnt exist is a no operation so dict remains the same [(3,3),(1,1),(4,4)]
   	self.result=cache.cache
   	self.expected=OrderedDict([(3,3),(1,1),(4,4)]) 
   	self.assertDictEqual(self.result,self.expected)

   	# The test will pass if both dictionaries has the same elements in correct order,recently accessed item will will go to end 
   def test_11(self):
   	cache=lruCache(3) # Setting the size 
   	cache.put(1,1)
   	cache.put(2,2) # Adding second item 
   	cache.put(3,3) # Adding third item 
   	cache.reset() # All the elements will be cleared 
   	self.result=cache.cache
   	self.expected=OrderedDict()# empty dictionary
   	self.assertDictEqual(self.result,self.expected)


   	# Trying to reset without adding any elements
   def test_12(self):
   	cache=lruCache(3) # Setting the size 
   	cache.reset() # Resetting 
   	self.result=cache.cache
   	self.expected=OrderedDict()# empty dictionary
   	self.assertDictEqual(self.result,self.expected)

   	# Deleting without adding any elements
   def test_13(self):
   	cache=lruCache(3) # Setting the size 
   	cache.delete(2) # Deleting,no operation
   	self.result=cache.cache
   	self.expected=OrderedDict()# empty dictionary
   	self.assertDictEqual(self.result,self.expected)

   # Returns true if it raises a KeyNotExistError 
   def test_14(self):
   	with self.assertRaises(Exception):
   		cache=lruCache(2) # Setting the size
   		cache.get(1)# Accessing key without Adding items  
  
if __name__ == '__main__':  
    unittest.main()