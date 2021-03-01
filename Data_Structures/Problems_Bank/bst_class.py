from node_class import Node

class BST():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        if self.root == None:
            return True
        return False
    
    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
        return ''
    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
        return ''
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
        return ''

    def tree_traversal(self, node, flag='pre'):
        if flag == 'pre':
            return self.preorder(self.root)
        elif flag == 'post':
            return self.postorder(self.root)
        elif flag == 'in':
            return self.inorder(self.root)
        else:
            return None
        

