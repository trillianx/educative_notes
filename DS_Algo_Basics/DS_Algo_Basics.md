[TOC]



# Basics of Data Structures 

These are my notes from the free online book, [A Common-Sense Guide to Data Structures and Algorithms](https://medium.com/pragmatic-programmers/table-of-contents-323f1846e259). 

## Data Structures

**Data** as a broad term refers to all types of information while **data structures** refer to how data is organized. Organization of data is important because it can significant impact how fast your code runs. So, depending on your choice of data structure, your code can run fast or slow.

### Performance of Data Structures

To understand the performance of any data structure, we need to analyze the common ways our code might interact with that data structure. Many data structures are used in four basic ways, which we refer to as operations: 

1.  **Read**: refers to looking up something at a particular spot within a data structure
2.  **Search**: searching for a particular value within a data structure
3.  **Insert**: adding a new value to our data structure
4.  **Delete**: removing a value from our data structure

In a given data structure, we evaluate how fast each of these operations are. 

### Measuring speed

The speed of a given operation is not measured in terms of time but instead in terms of the number of steps it takes. For example, consider two functions that output the even numbers between 1 and 100: 

```python
# Function 1
def find_even():
    result = [i for i in range(1, 101) if i%2 == 0]
    return result

# Function 2
def find_even():
    result = []
    i = 2
    while i != 100:
        result.append(i)
        i+= 2
    return result
```

We see that Function 2 takes half the steps of Function 1. Therefore, Funtion 2 is faster. 

So, why do we measure code speed in terms of steps? This is because measuring steps is agnositic to the computer hardware or software. Measuring the steps is known as the **time complexity**. Other tems used for time complexity are **efficiency, performance, runtime**. 

## Data Structure: Array

An array is a basic data structure in any given language. In python an array is represented by a `list`. A list is simply a data structure that is enclosed by square brackets. 

Here are some properties of an array: 

*   can contain mixed data structures
*   The index number locates the position of the element in the array
*   Index starts with `0`
*   The size of an array is given by the number of elements the array contains

Let's look at the speed of the four operations of this data structure. 

### Reading

In this data structure, a program is able to read a value directly when it knowns the index of the value. The computer is able to do this because each index maps to the location of the element in the computer's memory address. So, when you index an array, the computer finds the address of the element for that index and returns the value of element stored at that index. 

Given an array, such as: 

```python
['apples', 'bananas', 'cucumbers', 'dates', 'elderberries']
```

The computer stores these values as follows: 

![image-20210209105304422](DS_Algo_Basics.assets/image-20210209105304422.png)

As we can see the memery address is associated with each index. Notice how the memory addresses are consecutive or sequential. This helps the computer to easily find the address at a given index by simply adding memory address at `0` with that of a given index.

As we can see reading an element in an array takes one step, which is adding the index to the address at index `0`. When an operation takes one step, it is considered fast. 

### Searching

Searching is an inverse of reading. Rather than asking the computer to find the value at a given index, we ask it ito find the index of a value in a given array. 

Searching is tedious for the computer as there is no way for the computer to jump to that value. Instead, the computer has to go through each value, evaluate it, and then return an index if it finds the value. This way of finding a value in a given array is known as **linear search**. 

So, what is the maximum number of steps a computer needs to perform in order to linearly search a value in an array? We see that if the value we are looking for is at the first index, it takes just 1 step. This is the best scenario. However, if the element at the last index, it will take that many steps. This is the worst scenario. 

Therefore, if an array has N elements. The worst case scenario would be N steps. Clearly, we see that searching is not as fast as reading. 

### Insertion

The insertion operation depends on where we insert an element in the array. If the insertion happens at the end of the array, it is fairly quick. This is because the computer, simply needs to create a new address, which it can based on the index, and insert the value there. 

However, insertion at any other index is slower as it requires more than one step. Consider our list of veggies. Suppose we wish to enter `"figs"` just after `bananas`. In this case, we will have the following steps: 

1.  Create a new cell at the end
2.  Move each of the cells right of `bananas` by one to the right
3.  Insert `figs` in the empty cell, right of `bananans`

If we wish to insert at the beginning, the worst case scenario, we need to move all elements in the array to the right and then make an insertion. In short, given an array of size $N$, there would be $N+1$ steps to insert in the worst case scenario. 

### Deletion

The deletion operation involves finding the element, removing it and then moving all other elements, right of the element to the left. So, the deletion process is similar to insertion process. Therefore, if an array has $N$ elements, the deletion process will require, $N$ steps. 

## Data Structure: Sets

A set is a data structure that does not allow duplicate values to be contained within it. There are different types of sets but in this case we will talk about array-based sets. 

