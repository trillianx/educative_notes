class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
    



if __name__ == "__main__":
    bt = BinaryTree(7)
    bt.root.left = Node(3)
    bt.root.right = Node(6)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(8)
    bt.root.left.left = Node(9)
    