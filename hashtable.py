class HashTable(object):
    """
    for hash table (hash map) you can use python dictionary. 
    This is an implementation of hash map using linear probing and open addressing
    """
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        
    def hash_function(self, key):
        return key%self.size
    
    def rehash(self, oldhash):
        return (oldhash+1)%self.size
    
    def get_hash_after_collision_resolved(self, key):    
        hash_value = self.hash_function(key)
        i = 1
        if self.keys[hash_value] is None or self.keys[hash_value] == key:
            return hash_value
        else:
            while True:
                i = i + 1
                if i > self.size:
                    raise OverflowError("table is full. No open slot for new data! Increase the table size")
                rehashed_key = self.rehash(hash_value)
                if self.keys[rehashed_key] is None or self.keys[rehashed_key] == key:
                    return rehashed_key
                else:
                    hash_value = rehashed_key
                
    def put(self, key, value):
        """
        this method put a (key, value) into the hash table. It calculates the hash and uses
        linear probing to find the key. If key does not exists it insert the key value in open 
        addressing fashion. If key does exist, it update the value.
        """
        hash_value = self.get_hash_after_collision_resolved(key)
        self.keys[hash_value] = key
        self.values[hash_value] = value
    
    def get(self, key):
        hash_value = self.get_hash_after_collision_resolved(key)
        return self.values[hash_value]
            
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    
H = HashTable(11)
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
H[20]="chicken"

print H.keys
print H.values

print H[20]
print H[17]
H[20]='duck'
print H[20]