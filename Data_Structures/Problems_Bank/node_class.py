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
    
    def search(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def delete(self, value):
        # if current node's val is less than that of root node,
        # then only search in left subtree otherwise right subtree
        if value < self.data:
            if(self.left):
                self.left = self.left.delete(value)
            else:
                print(str(value) + " not found in the tree")
                return self
        elif value > self.data:
            if(self.right):
                self.right = self.right.delete(value)
            else:
                print(str(value) + " not found in the tree")
                return self
        else:
            # deleting node with no children
            if self.left is None and self.right is None:
                self = None
            # Delete node with no left child
            elif self.left is None:
                return self.right
            # Delete node with no right child
            elif self.right is None:
                return self.left
        return self
