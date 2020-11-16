class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self, value, self.root)
    
    def _insert(self, value, cur.node):
        if value < cur.node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur.node.value:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value in BST")

    def inorder(self, node):
        if node:
            self.inorder(self, node.left)
            print(node.data)
            self.inorder(self, node.right)
        return ''

    def show(self):
        if self.root != None:
            self.inorder(self.root)

