class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        self.head = new_node
        return

ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(20)
