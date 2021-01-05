[TOC]



# Practice Problems

Here is a list of fundamental problems that are often asked in Coding Interviews. These are the problems that you should be able to do quickly. The problems are arranged by data structures used. 



## Arrays





## Stacks

Here we include the common and interesting problems on Stacks

### Write a method to find a minimum value in a Stack with $O(1)$. 

The key idea is to make use of two stacks. One keeps only the minimum value while the other keeps just the minimum value. 

```python
class Stack():
    def __init__(self):
        self.array = []
        self.array_min = []
        
    def pop(self):
        if self.array != []:
            return self.array.pop()
        else:
            return None
        
    def push(self, value):
        if self.array == []:
            self.array_min.append(value)
        else:
            if value < self.array_min[-1]:
                self.array_min.pop()
                self.array_min.append(value)
            self.array.append(value)
    
    def min(self):
        return self.array_miin.pop()
```

## Write a method `stack_sort()` to sort a Stack

It can easily be done with the `.sort()` method on an array. But do not use this or any other sorting method. 

The trick here is to use one more stack and juggle the numbers between these two stacks. It is also important to keep the order in one stack such that the top has the highest number such that when you unstack, you get the smallest on top. 

```python
from stack_class import Stack

def sort_stack(s):
    temp_stack = Stack()

    while not s.isEmpty():
        value = s.pop()

        if temp_stack.top() is not None and value >= temp_stack.top():
            temp_stack.push(value)
        else:
            while not temp_stack.isEmpty():
                s.push(temp_stack.pop())
            temp_stack.push(value)

    while not temp_stack.isEmpty():
        s.push(temp_stack.pop())
    
    return s
```



