

# Recursion Tricks

Through my learning data structures and algorithms, I have come across some interesting recursion tricks, which I list here: 

## Counting with Recursion

This is the easiest but is used often. 

Question: Given an array, count the number of elements in the array: 

```python
arr = [4,9,5,2,8,12,10,14,-1]

def count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count(arr[1:])
```

This technique is particularly helpful when finding the **height of a BST**. 

## Creating a List using Recursion

Suppose you have a function that outputs values. You wish to capture those values into a list using recursion. 

```python
def get_random_values(count):
    arr = []
    _get_recursive(count, arr)
    return arr
    
def _get_recursive(count, arr):
    if count == 0:
        return 
    _get_recursive(count-1, arr)
    arr.append(random.randint(1, 10))
    
```

This technique is particularly helpful when finding the **kth maximum in a BST**. 

