[TOC]



# Tree Problems for Practice

## Easy 

### 1. Write a binary tree class

Here you will define a simple binary tree class. 

### 2. Check if the tree is empty

Here we are not looking at whether a given node is empty, rather if the entire tree is empty. 

### 3. Write the basic tree traversal: preorder, postorder, inorder

Write these are three separate functions. Should they be methods? 

### 4. Write a method to insert a value in a BST

Where would this method be? In BST class or Node class? 

## Medium





# Solutions

## Easy

### 1. Write a Binary Tree class

```python
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
class BST():
    def __init__(self, data):
        self.root = Node(data)
    
```

### 2. Check if the tree is empty

To check that we will use a method in the `BST` class: 

```python
def isEmpty(self):
    if self.root == None:
        return True
    return False
```

Here we use `self.root.left` instead of `self.left` because the `BST()` class does not have `self.left`. But `root` which is a node has it.

### 3. Write the basic tree traversal: preorder, postorder, inorder

These tree traversal are written in the `BST` class:

```python
# This would be in the BST class: 
def preorder(self, node):
    if node is not None:
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)
    else:
        return ''

def inorder(self, node):
    if node is not None:
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
    else:
        return ''
    
def postorder():
    if node is not None:
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)
    else:
        return ''

def tree_traversal(self, flag):
    if flag == 'pre':
        return self.preorder(self.root)
    elif flag == 'in':
        return self.inorder(self.root)
    elif flag == 'post':
        return self.postorder(self.root)
```



### 4. Write a method to insert a value in a BST

