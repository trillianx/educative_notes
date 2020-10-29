class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        # Append at tail
        new_node = Node(data)
        if self.isEmpty():
            self.prepend(data)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur


    def prepend(self, data):
        # Append at head
        new_node = Node(data)
        new_node.prev = None
        new_node.next = self.head
        self.head = new_node
        return

    def show(self):
        if not self.isEmpty():
            cur = self.head
            while cur != None:
                print(cur.data)
                cur = cur.next
        else:
            return None

if __name__ == "__main__":
    dl = DoublyLinkedList()
    dl.prepend(35)
    dl.prepend(25)
    dl.show()
    dl.append(15)
    dl.show()