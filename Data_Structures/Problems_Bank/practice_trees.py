from node_class import Node
from bst_class import BST
from display_tree import display


if __name__ == '__main__':
    b = BST()
    print(b.isEmpty())
    arr = [9, 4, 17, 3, 6, 18, 19]
    for a in arr:
        b.insert(a)
    display(b.root)
    print(b.delete(17))
    print(" ")
    print("-"*20)
    print(" ")
    display(b.root)
