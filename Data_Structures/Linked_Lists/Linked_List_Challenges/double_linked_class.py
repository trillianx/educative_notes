class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head_node = None

    def isEmpty(self):
        return self.head_node == None

    def append(self, data):
        # Append at tail
        new_node = Node(data)
        if self.isEmpty():
            self.insert_at_head(data)
        else:
            cur = self.head_node
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None


    def insert_at_head(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head_node = new_node
            return
        new_node.next = self.head_node
        self.head_node.prev = new_node
        self.head_node = new_node
        return

    def get_size(self):
        if self.isEmpty():
            return 0
        count = 0
        cur = self.head_node
        while cur is not None:
            count = count + 1
            cur = cur.next

        return count


    def show_right(self):
        if not self.isEmpty():
            cur = self.head_node
            while cur != None:
                print(cur.data)
                cur = cur.next
        else:
            return None

    def show_left(self):
        if not self.isEmpty():
            cur = self.head_node
            while cur.next != None:
                cur = cur.next
            prev_node = cur
            print(prev_node.data)
            while prev_node.prev != None:
                prev_node = prev_node.prev
                print(prev_node.data)
        else:
            return None
        return

if __name__ == "__main__":
    dl = DoublyLinkedList()
    dl.insert_at_head(35)
    dl.insert_at_head(25)
    for i in range(5):
        dl.append(i)
    # print("")
    dl.show_right()
    print("")
    dl.show_left()
    # print(dl.get_size())