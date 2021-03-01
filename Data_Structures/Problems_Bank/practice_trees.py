from node_class import Node
from bst_class import BST


if __name__ == '__main__':
    b = BST()
    print(b.isEmpty())
    arr = [9, 4, 17, 3, 6]
    for a in arr:
        b.insert(a)
    print(b.preorder(b.root))
