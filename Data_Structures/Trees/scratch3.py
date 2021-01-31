from new_bst import BST
from new_bst import Node

def find_height(b):
    if b.root is None:
        return 0
    else:
        return _find_height(b.root, 0)

def _find_height(b, count):
    if b.left and b.right:
        return max(_find_height(b.left, count+1), _find_height(b.right, count+1))
    elif b.left:
        return _find_height(b.left, count+1)
    elif b.right:
        return _find_height(b.right, count+1)
    else:
        return count

def find_max(b):
    if b.root:
        return _find_max(b.root)
    else:
        return 0

def _find_max(b):
    if b.right:
        return _find_max(b.right)
    else:
        return b.data

def find_kth_max(b, k):
    arr = []
    inorderTraverse(b.root, arr)
    if k <= len(arr):
        return arr[-k]

def inorderTraverse(node, arr):
    if node:
        inorderTraverse(node.left, arr)
        arr.append(node.data)
        inorderTraverse(node.right, arr)


if __name__ == "__main__":
    b = BST()
    arr = [4,9,5,2,8,12,10,14, -1]
    for i in arr:
        b.insert(i)
    # print(find_height(b))
    print(b.inorder())
    print(find_kth_max(b, 2))