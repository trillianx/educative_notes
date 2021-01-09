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

def resize(self):
    new_slots = self.slots * 2
    new_bucket = [None] * new_slots
    # Now go through each bucket and add them into new buckets
    for i in range(len(self.bucket)):
        head = self.bucket[i]
        while head is not None:
            new_index = hash(head.key) % new_slots
            if new_bucket[new_index] is None:
                new_bucket[new_index] = HashEntry(head.key, head.value)
            else:
                node = new_bucket[new_index]
                while node is not None:
                    if node.key is head.key:
                        node.value = head.value
                        node = None
                    elif node.next is None:
                        node.next = HashEntry(head.key, head.value)
                        node = None
                    else:
                        node = node.next
            head = head.next
    self.bucket = new_bucket
    self.slots = new_slots