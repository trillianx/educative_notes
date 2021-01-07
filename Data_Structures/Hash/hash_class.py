class HashEntry():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
class HashTable():
    def __init__(self):
        self.slots = 10
        self.size = 0
        self.bucket = [None] * self.slots

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.get_size() == 0

    def get_index(self, key): # This is a hash function
        hash_code = hash(key)
        index = hash_code % self.slots
        return index