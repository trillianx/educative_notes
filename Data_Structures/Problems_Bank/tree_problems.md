[TOC]



# Tree Problems for Practice

## Easy 

### 1. Write a binary tree class

Here you will define a simple binary tree class. 

### 2. Check if the tree is empty

Here we are not looking at whether a given node is empty, rather if the entire tree is empty. 

### 3. Write the basic tree traversal: preorder, postorder, inorder



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
    if self.root.left == None and self.root.right == None:
        return True
   	return False
    
```

### 3. Write the basic tree traversal: preorder, postorder, inorder

These tree traversal are written in the `BST` class: 

```python
def preorder(self):
    
```

