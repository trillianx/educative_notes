[TOC]



# Tree Problems for Practice

## Easy 

### 1. Write a binary tree class

Here you will define a simple binary tree class. 

### 2. Check if the tree is empty

Here we are not looking at whether a given node is empty, rather if the entire tree is empty. 

### 3. Write the basic tree traversal: pre-, post-, in-order

Write these are three separate functions. Should they be methods? 

### 4. Write a method to insert a value in a BST

Where would this method be? In BST class or Node class?

### 5. Write a method to search for a value in BST

So, given a value, the method should return either true or false based on whether the value exists or not. 

### 6. Delete A Leaf Node

Write a method to delete a leaf node in a given tree

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

### 3. Write the basic tree traversal: pre-, post-, in-order

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

```python
# This would be in node class

def insert(self, value):
    if value < self.data:
        if self.left is not None:
            self.insert(value)
        else:
            node.left = Node(value)
    elif value > node.data:
        if self.right is not None:
            self.insert(value)
        else:
            self.right = Node(value)
    else:
        print('Value already in BST')
        
# This would be in the BST Class: 

def insert(self, value):
    if self.root:
        self.root.insert(value)
   	else:
        self.root = Node(value)Write a method to search for a value in BST
```

### 5. Write a method to search for a value in BST

```python
# In BST Class:
def search(self, value):
    if not self.isEmpty():
        return self.root.search(value)
    else:
        return False
    

# In Node Class:
def search(self, value):
    if value == self.data:
        return True
    elif value < self.data:
        if self.left:
            return self.left.search(value)
        else:
            return False
    elif value > self.data:
        if self.right:
            return self.right.search(value)
        else:
            return False
```

