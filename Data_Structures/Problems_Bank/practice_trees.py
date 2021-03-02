from node_class import Node
from bst_class import BST
from display_tree import display


if __name__ == '__main__':
    b = BST()
    print(b.isEmpty())
    arr = [9, 4, 16, 3, 6, 19, 15, 18, 20]
    for a in arr:
        b.insert(a)
    display(b.root)
    b.delete(16)
    print(" ")
    print("-"*20)
    print(" ")
    display(b.root)
