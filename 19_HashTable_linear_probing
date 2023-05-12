class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
    
    def hash_function(self, key):
        """Hashes a key using a simple hash function."""
        return key % self.size
    
    def insert(self, key, value):
        """Inserts a key-value pair into the hash table."""
        hash_value = self.hash_function(key)
        if self.keys[hash_value] is None:
            self.keys[hash_value] = key
            self.values[hash_value] = value
        else:
            # Linear probing to find an empty slot
            next_slot = (hash_value + 1) % self.size
            while self.keys[next_slot] is not None and self.keys[next_slot] != key:
                next_slot = (next_slot + 1) % self.size
            if self.keys[next_slot] is None:
                self.keys[next_slot] = key
                self.values[next_slot] = value
            else:
                # Key already exists in the hash table, update the value
                self.values[next_slot] = value
    
    def get(self, key):
        """Returns the value associated with the given key."""
        hash_value = self.hash_function(key)
        if self.keys[hash_value] == key:
            return self.values[hash_value]
        else:
            # Linear probing to find the key
            next_slot = (hash_value + 1) % self.size
            while self.keys[next_slot] is not None and self.keys[next_slot] != key:
                next_slot = (next_slot + 1) % self.size
            if self.keys[next_slot] == key:
                return self.values[next_slot]
            else:
                raise KeyError(f'Key {key} not found in hash table.')
    
    def delete(self, key):
        """Deletes the key-value pair associated with the given key."""
        hash_value = self.hash_function(key)
        if self.keys[hash_value] == key:
            self.keys[hash_value] = None
            self.values[hash_value] = None
        else:
            # Linear probing to find the key
            next_slot = (hash_value + 1) % self.size
            while self.keys[next_slot] is not None and self.keys[next_slot] != key:
                next_slot = (next_slot + 1) % self.size
            if self.keys[next_slot] == key:
                self.keys[next_slot] = None
                self.values[next_slot] = None
            else:
                raise KeyError(f'Key {key} not found in hash table.')
