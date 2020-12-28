

# Arrays

An array is also called a **list**. In python a list is an ordered sequence of heterogeneous elements. Here's an example of  a list: 

```python
list = ['a', 'apple', 23, 3.14, [24, 'a', 49]]
```

As we can see lists can hold literally any data structure. It can also hold functions. Lists are **indexed** using index `0`, which would be the first element and so on. 

There are two ways to initialize a list: 

*   Use of square brackets
*   Use of the function `list()`. 

## Important List Functions

The table below shows some of the important list functions that are used: 

| Function    | Explanation                                                  | Time Complexity  |
| ----------- | ------------------------------------------------------------ | ---------------- |
| `append()`  | Added a single element to the end of the list                | $O(1)$           |
| `insert()`  | Inserts an element at a specific index                       | $O(n)$           |
| `remove()`  | Removes a specific element from list                         | $O(n)$           |
| `pop()`     | Removes an element at given index or the last element if no index given | $O(1)$ or $O(k)$ |
| `reverse()` | Reverses the list                                            | $O(n)$           |

Here are some examples for each of the functions: 

```python
l = [24, 54, 9]

# Append to a list
l.append('a')

# Insert to a list
l.insert(2, 100)

# Remove from a list.
# You'll get runtime error is element does not exist
l.remove('a')

# Pop
l.pop()       # <- this will remove the last element
l.pop(2)      # <- this will remove the third element

# reverse
l.reverse()    # <- reverse function reverses a list in place
```

## Slicing

Slicing is done to create sublists. The general syntax for slicing is the following: 

```python
the_list[start_index:end_index:step]
```

>   When a sublist is created, all the elements from the `start_index` up until but not inclusive of the `end_index` are included. 

For example, 

```python
a = [100, 2, 43, 99, 73, 45]
print(a[1:5])

[2, 43, 99, 73]
```

We see that `45` is at index `5` but it is not included in the list. 

Arrays also allow for step indexing. The general syntax is: 

```python
a = list(range(10))
print(a)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Suppose we wish to only print out even numbers: 
print(a[::2])

[0, 2, 4, 6, 8]
```

List is a mutable object so the elements can easily be changed through slicing. 

```python
a[5:9] = [100, 200, 300, 400]
print(a)

[0, 1, 2, 3, 4, 100, 200, 300, 400, 9]
```

You can use a function `del` to delete a sublist from a list. This will remove all the elements from the sublist which are also in the main list: 

Suppose we wish to only get odd numbers from our list `a`:

```python
a = list(range(10))
print(a)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del a[::2]

print(a)

[1, 3, 5, 7, 9]
```

Arrays also provide us with **negative indexing**. A negative index starts from the end of the list. 

```python
# Get the first three elements: 
print(a)

[1, 3, 5, 7, 9]

print(a[:-2])

[1, 3, 5]
```

