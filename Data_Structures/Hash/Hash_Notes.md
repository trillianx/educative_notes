[TOC]



# Hash Tables

The data structures such as arrays, linked lists, stacks, queues, and trees have an overall time complexity of $(Ologn)$ or $O(nlogn)$ for opertions such as: 

*   Insertion
*   Deletion
*   Search

For small $n$, this does not pose a problem but when $n$ increases, this begins to turn into a challenge. We wish to find a data structure that takes constant time to perform these operations. This is where the hashing data structure comes into the spotlight. 

Hashing is a process to store an object according to a unique key. This means that hashing always creates a **key-valule pair**. A collection of such pairs forms a dictionary where every object or value can be looked up according to its key. Hence, the search operation can be performed in $O(1)$. 

In python hash tables are generally implemented using lists as they provide access to elements in constant time.  A hash table in Python is a **dictionary**, a data structure that is composed of a **key-value** pair. There are two built-in types that exist in Python, `set()` and `dict()`. 

Rather than using an built-in hash table that Python has, we will build our own hash table as it is very popular topic in coding interviews. We start by defining the building blocks on an efficient hash table. 

The performance of a hash table depends on three fundamental factors: 

1.  Hash Function
2.  Size of the hash table
3.  Collision handling method

## The Hash Function

We start with the first building block, the hash function. 

The data is stored in a list and a key is used to map the value on the list. The efficiency of the hash table depends on how the key is computed. We could simply use index of a list as a key. Though this may work as the index is unique, this process will fail when the key exceeds the length of the list. We could resize the list and therefore continue to use the index but resizing of a list takes $O(n)$ time. 

In order to limit the range of the keys to the length of the list, we need a function that converts a large key into a smaller key. This is done by the **hash function**. 

![image-20210107100820691](Hash_Notes.assets/image-20210107100820691.png)

A hash function simply takes an item's key and returns the corresponding index in the list for that item. This process can simply be arithmetic or a complicated encryption method. Nonetheless, the hash function needs to be efficient. 

Let's look at some hash functions used. 

### Arithmetic Modular

Such a hash function maps the keys such that they are within the size of list. This is done by taking the mod of the key with the size of the list. 
$$
index = key \ MOD \ table\_size 
$$
This allows the index to always lie between the boundaries of the list. 

```python
def hash_modular(key, size):
    return key % size


if __name__ == "__main__":
    lst = [False] * 10
    key = 35
    index = hash_modular(key, len(lst))
    print(index)
```

This will return an index of `5`. So, even though `35` was outside of the size of the list, we were able to add that to the list. 

### Truncation

Another hash function is to take the key and truncate it. 
$$
key = 123456 -> \ index = 3456
$$

```python
def hash_truncate(key):
    return key % 1000  # this gives us a key of up to 3 digits

if __name__ == "__main__":
    lst = [False] * 10
    key = 1235433
    index = hash_truncate(key)
    print(index)
```

In this example, we get `433`, the last three digits. 

### Folding

Another hash function is to take the key, break it into smaller chunks, and add them up to create an index. 

```python
def hash_fold(key, chunk_size):
    str_key = str(key)  # Convert integer into string for slicing
    print("Key: " + str_key)
    hash_val = 0
    print("Chunks:")
    for i in range(0, len(str_key),  chunk_size):

        if(i + chunk_size < len(str_key)):
            # Slice the appropriate chunk from the string
            print(str_key[i:i+chunk_size])
            hash_val += int(str_key[i:i+chunk_size])  # convert into integer
        else:
            print(str_key[i:len(str_key)])
            hash_val += int(str_key[i:len(str_key)])
    return hash_val

if __name__ == "__main__":
    key = 3456789
    chunk_size = 2
    print(hash_fold(key, chunk_size))
```

This returns the following: 

```python
Key: 3456789
Chunks:
34
56
78
9
177
```

### Collisions in Hash Tables

When you map large keys into a small range of numbers from 0-N where $N$ is the size of the list, there is a possibility of two different keys mapping to the same index. This is called **collision**. 

![image-20210107103916870](Hash_Notes.assets/image-20210107103916870.png)

There are ways to avoid this from happening. The three most common strategies are: 

*   Linear Probing
*   Chaining
*   Resizing the list

Let's look at them in more detail. 

#### Linear Probing

This suggests that if the hash function returns an index that is already filled, move to the next index. The next is based on an offset, which we set. If that index is also filled to move to the next. Do this until an empty index is found. Now the choice of offset is important. If chosen wrongly, we may end up where we started. 

Let's look at an example. Our size of a list is 20. We decide to use a modular hash function. So, when the key is 2 and the key is 42, we get the same index. So, we have a collision. Let's see our offset is 4. So, when 42 key is mapped, we get a collision at 2 but with the offset we have a new index of 6, which is empty. 

![image-20210107104625844](Hash_Notes.assets/image-20210107104625844.png)

#### Chaining

In this strategy, each slot in the hash table holds a pointer to another data structure such as a linked list or a tree. Every entry at that index will be inserted into the linked list for that index. This allows us to add multiple key-pair values to the same index in constant time. 

<img src="Hash_Notes.assets/image-20210107105025054.png" alt="image-20210107105025054" style="zoom:50%;" />

This strategy works but it adds more space. 

#### Resizing the List

This involves increasing the size of the list when the list is filled to a certain threshold. By convention we use 0.6. So, when 60% of the list is filled, we resize. However, resizing can be expensive therefore the threshold must be chosen carefully. Another thing to keep in mind is that the content might be concentrated at one end of the list and resizing will not pick this up. 

Some other strategies to handle collisions are: 

*   quadratic probing
*   bucket method
*   random probing
*   key rehashing

## Building a Hash Table from Scratch

In our implementation of hash table, we will use the chaining strategy along with the resize operation to avoid collisions in the table. 

All the elements with the same hash key will be stored in a linked list at that index. This is called bucketing. The size of the hash table is set as $n \times m$ where $n$ is the number of keys it can hold and $m$ is the number of slots each bucket contains. Each slot holds a key-value pair. 

![image-20210107134237797](Hash_Notes.assets/image-20210107134237797.png)

We will start by building a simple `HashEntry()` class. It has three data members:

*   key
*   value
*   reference to a new entry

```python
class HashEntry():
    def __init__(self, key, data):
        self.key = key
        self.value = value
        self.next = None
        
```

Now we will create a `HashTable()` class which is a collection of `HashEntry()` objects. In this case we keep track of two variables: 

*   Total number of slots in the table
*   Current size of the table

These two will become handy when we need to resize the table. 

```python
class HashTable():
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.get_size() == 0

    # This is a hash function
    def get_index(self, key):
        # hash() is a built-in function in python
        hash_code = hash(key)
        index = hash_code % self.slots
        return index
```

 ### Resizing the Hash Table

To start off we will first ensure that the hash table does not get loaded beyond a certain threshold. When it crosses a threshold, we shift the elements from the current table to a new table with double capacity. this helps avoid collision. 

So, let's implement the `resize()` function. 

```python
def resize(self):
    new_slots = self.slots * 2
    new_bucket = [None] * new_slots
    # Now go through each bucket and add them into new buckets
    for i in range(len(self.bucket)):
        head = self.bucket[i]
        while head is not None:
            new_index = hash(head.key) % new_slots
            if new_bucket[new_index] is None:
                new_bucket[new_index] = HashEntry(head.key, head.value)
            else:
                node = new_bucket[new_index]
                while node is not None:
                    if node.key is head.key:
                        node.value = head.value
                        node = None
                    elif node.next is None:
                        node.next = HashEntry(head.key, head.value)
                        node = None
                    else:
                        node = node.next
            head = head.next
    self.bucket = new_bucket
    self.slots = new_slots
             
```











The operations we implemented for hash tables have the following time complexity:

![image-20210107143358535](Hash_Notes.assets/image-20210107143358535.png)

### Comparison Between Trees and Hash Tables

Hash tables perform search, insertion, and deletion in constant time whereas trees usually work in $O(log n)$. In the worst case, the performance of hash tables in $O(log\ n)$. An AVL tree would maintain $O(log\ n)$ even in the worst case. 

If an application requires the data to be ordered in a specific sequence, trees would be more useful because a BST or an AVL tree maintains order. Hash tables work best when the data stored is in random order. 

### Difference between Dict and Set in Python

*   Dict
    *   Stores `key-value` pairs
    *   Cannot contain duplicate keys but can have duplicate values
    *   Does not store elements in any order It takes the key and then maps it into the range of hash table using the hash function
    *   On average, the time complexity is $O(1)$
*   Set
    *   Is not a `key-value` pair, instead the value is the key and the value
    *   Set does not store duplicate elements
    *   On average, the complexity of basic operation is $O(1)$

Here are some common functions for both these data structures

<img src="Hash_Notes.assets/image-20210107144953542.png" alt="image-20210107144953542" style="zoom:50%;" />

<img src="Hash_Notes.assets/image-20210107145006664.png" alt="image-20210107145006664" style="zoom:50%;" />



## Problem Sets

Here are a total of 12 interview problems on hash tables

### Challenge 1: A List as a Subset of Another List

Given two lists, write a function `is_subset(lst1, lst2)` check whether one is a sublist of another. 

For example, 

```python
list1 = [9,4,7,1,-2,6,5]
list2 = [7,1,-2]
```

The response is: `True`

![image-20210107145507908](Hash_Notes.assets/image-20210107145507908.png)



```python
def is_subset(lst1, lst2):
    s1 = set(lst1)
    s2 = set(lst2)
    result = s1.intersection(s2)
    if len(result) == len(lst2):
        return True
    else:
        return False
    
if __name__ == "__main__":
    list1 = [9, 4, 7, 1, -2, 6, 5]
    list2 = [7, 1, -2]
    list3 = [10, 12]
    print(is_subset(list1, list2))
    print(is_subset(list1, list3))
```

