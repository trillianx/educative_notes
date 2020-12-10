class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    # Check if the Linked List is Empty
    def isEmpty(self):
        return self.head == None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self.head
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.insert_at_head(data)
            return

        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next

        cur_node.next = new_node
        return
        
    def get_length(self):
        if self.isEmpty():
            return 0
        count = 0
        cur_node = self.head
        while cur_node != None:
            count += 1
            cur_node = cur_node.next
        return count

    def insert_at_index(self, index, data):
        if self.isEmpty():
            self.insert_at_head(data)
            return
        
        count = 0
        cur_node = self.head
        
        while count < index:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        
        new_node = Node(data)
        prev.next = new_node
        new_node.next = cur_node
        return
    
    def print_ll(self):
        if self.isEmpty():
            return
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next
        return

