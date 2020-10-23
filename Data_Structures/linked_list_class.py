from node_class import Node

class LinkedList():
    def __init__(self):
        self.head_node = None
    
    def get_head(self):
        if self.head_node is not None:
            return self.head_node
        return self.head_node

    def isEmpty(self):
        if self.head_node is None:
            return True
        else:
            return False
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head_node
        self.head_node = new_node
        return self.head_node

    def insert_at_tail(self, data):
        
        new_node = Node(data)

        # Check if the linked list is empty: 
        if self.head_node is None:
            self.head_node = new_node
            return

        # If the linked list is not empty:     
        cur_node = self.head_node
        while cur_node.next != None:
            cur_node = cur_node.next
        
        cur_node.next = new_node
        return

    def len(self):
        if self.head_node is None:
            return 0
        count = 0
        curr = self.head_node
        while curr is not None:
            curr = curr.next
            count += 1
        return count

    def insert_at_index(self, index, data):
        new_node = Node(data)
        
        # Check if the linked list is empty
        if self.isEmpty():
            self.insert_at_head(data)
            
        n = self.len()
        if index > n:
            return 'Index out of range'
        elif index == n:
            return self.insert_at_tail(data)
        else:
            count = 0
            curr = self.head_node
            while count < index:
                print(count)
                prev = curr
                curr = curr.next
                count += 1
        # Point the previous to new node:
        new_node.next = curr
        prev.next = new_node
        return 


    def show(self):
        cur_node = self.head_node
        print(cur_node.data)
        while cur_node.next != None:
            cur_node = cur_node.next
            print(cur_node.data)