from binary_tree_class import Node
from binary_tree_class import BinaryTree


def traverse_left(bt):
    if bt.root.left == None:
        return
    else:
        print(bt.root.left.data)
        return traverse_left(bt.root.left)

if __name__ == "__main__":
    bt = BinaryTree(7)
    bt.root.left = Node(3)
    bt.root.right = Node(6)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(8)
    bt.root.left.left = Node(9)
    traverse_left(bt)