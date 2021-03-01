class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.data:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = Node(value)
        elif value > self.data:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = Node(value)
        else:
            print('Value already exists')
    
