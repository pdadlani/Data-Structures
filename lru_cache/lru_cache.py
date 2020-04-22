import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # limit represents max number of nodes the cache can hold
        self.limit = limit
        # size represents the current number of nodes in cache
        self.size = 0
        # pairs is a DLL that holds the key-value pairs
        self.pairs = DoublyLinkedList()
        # storage allows for quick access / search of key-value pair
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if the key exists
        if key in self.storage:
            # save it's data / entire node to a variable
            node = self.storage[key]
            # so you can move the node to the end of the DLL
            # making it 'mose-recently used'
            self.pairs.move_to_end(node)
            # return the data you want
            return node.value[1]
        # if the key does not exist, return None
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if the key is in the existing data structure
        if key in self.storage:
            # get the node, update the value of the node, and move to end of dll
            node = self.storage[key]
            node.value = (key, value)
            self.pairs.move_to_end(node)
            return

        # if the cache is filled
        if self.size == self.limit:
            # delete the oldest data point, aka the one at the front of the DLL & in the dict
            # and decrement the size
            del self.storage[self.pairs.head.value[0]]
            self.pairs.remove_from_head()
            self.size -= 1


        # otherwise, knowing there is space
        # add this new key-value pair, and increment the size
        self.pairs.add_to_tail((key, value))
        self.storage[key] = self.pairs.tail
        self.size += 1


cache = LRUCache(3)
cache.set('1', 'a')
cache.get('1')
cache.set('2', 'b')
cache.set('3', 'c')
cache.set('2', 'wtf')
