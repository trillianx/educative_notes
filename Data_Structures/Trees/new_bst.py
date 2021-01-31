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

    def search(self, value):
        print(self.data)
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
        else:
            return True
        return False  
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                print('Before: ', self.left.data)
                self.left = self.left.delete(value)
                print('After: ', self.left.data)
            else:
                print("Value not found: ", value)
                return None
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
            else:
                print("Value not found: ", value)
                return None
        else:
            # The value is found! 
            # Delete a node with no children
            if self.left is None and self.right is None:
                self = None
                return None
            # Delete a right child only
            elif self.left is None:
                tmp = self.right
                self = None
                return tmp
            # Delete a left child only
            elif self.right is None:
                tmp = self.left
                self = None
                return tmp
            # Delete a node with two children
            else:
                current = self.right
                while current.left is not None:
                    current = current.left
                self.data = current.data
                self.right = self.right.delete(value)
        return self
        
class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)
        
    def search(self, value):
        if self.root is None:
            return False
        else:
            return self.root.search(value)
        
    def delete(self, value):
        if self.root is not None:
            self.root.delete(value)

    def inorder(self):
        if self.root:
            return self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data)
            self._inorder(node.right)
        return ''

if __name__ == "__main__":
    arr = [6, 4, 9, 5, 2, 8, 12]
    b = BST()
    for a in arr:
        b.insert(a)
    print(b.inorder())