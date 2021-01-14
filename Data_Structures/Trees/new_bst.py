class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
        else:
            print("Value " + str(value) + " already in BST")
            return None
    
class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)
        

