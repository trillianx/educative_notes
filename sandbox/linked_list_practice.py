import numpy as np
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

    def find_at_index(self, index):
        length = self.get_length()
        if index > length:
            return
        count = 0
        cur_node = self.head
        while count != index:
            cur_node = cur_node.next
            count += 1
        if cur_node != None:
            return cur_node.data

    def find_middle(self):
        length = self.get_length()
        print(length)
        middle = length / 2
        if length % 2 == 0:
            middle = int(middle)
        else:
            middle = int(np.round(middle))
        
        return self.find_at_index(middle)

    def delete_at_index(self, index):
        if self.isEmpty():
            return
        if index > self.get_length():
            return
        count = 0
        cur_node = self.head
        while count < index:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
        prev_node.next = cur_node.next
        return

        

