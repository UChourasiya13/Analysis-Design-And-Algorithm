class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
 
    def hash_function(self, key):
        """
        A simple hash function that uses the length of the key to generate an index
        """
        return len(key) % self.size
 
    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table
        """
        index = self.hash_function(key)
        self.table[index].append((key, value))
 
    def search(self, key):
        """
        Searches the hash table for a given key and returns the corresponding value
        """
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)
 
    def remove(self, key):
        """
        Removes a key-value pair from the hash table
        """
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        raise KeyError(key)
