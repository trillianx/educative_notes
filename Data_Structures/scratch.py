class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def show_recur(self, node):
        if node:
            print(node.data)
            return self.show_recur(node.next)

    def run(self):
        return self.show_recur(self.head)
        

    def show(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next
        return ''

ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_head(30)
print(ll.show())
