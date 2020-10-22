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

    def show(self):
        cur_node = self.head_node
        print(cur_node.data)
        while cur_node.next != None:
            cur_node = cur_node.next
            print(cur_node.data)
            

if __name__ == "__main__":
    ll = LinkedList()
    print(ll.get_head())
    ll.insert_at_head(25)
    ll.insert_at_head(35)
    ll.insert_at_head(45)
    ll.insert_at_head(55)
    ll.show()
    print("--"*10)
    ll.insert_at_tail(15)
    ll.show()