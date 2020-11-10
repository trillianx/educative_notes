class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, data):
        self.root = Node(data)
        
    def is_empty(self):
        if self.root.left == None and self.root.right == None:
            return True
        else:
            return False
    
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

    def run(self, flag):
        if flag == 'preorder':
            return self.preorder(self.root)
        elif flag == 'postorder':
            return self.postorder(self.root)
        elif flag == 'inorder':
            return self.inorder(self.root)
        else:
            return None


if __name__ == "__main__":
    bt = BinaryTree(1)
    bt.root.left = Node(2)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right = Node(3)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(7)
    #print(bt.run('preorder'))
    #print(bt.run('postorder'))
    print(bt.run('inorder'))
