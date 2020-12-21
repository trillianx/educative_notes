[TOC]



# Heap

## Introduction

Heaps are advance data structures that are useful for problems involving sorting and implementing priority queues. 

>   Heaps are regular binary trees with two special properties: 
>
>   1.  Heaps must be **Complete Binary Trees**
>   2.  The nodes must be ordered according to the Heap Order Priority

Let's look at each of these two properties in more detail. 

### Heaps must be Complete Binary Trees

A **complete binary tree** is a tree that has at most two children and the nodes at all levels are full, except for the leaf nodes, which can be empty. Here are some properties of complete binary trees: 

1.  All leaves are either at depth $d$ or depth $d-1$. 
2.  The leaves at depth $d$ are to the left of the leaves at depth $d-1$. 
3.  There are at most one node with just one child
4.  If the singular child exists, it is the left child of its parent
5.  If the singular child exists, it is the right most leaf at depth $d$

Here's an example of complete binary tree and incomplete one. 

![image-20201221094645631](Heap_Notes.assets/image-20201221094645631.png)

### Nodes Must be Ordered According to Heap Order Property

The heap order property depends on the two heap data structures: 

*   **Min Heap** - all parent node keys are less than or equal to their child node keys. So, the root will always contain the smallest element in the heap.  
*   **Max Heap** - all the parent node keys must be greater than or equal to their child node keys. In order words, the root node will always contain the largest element in the Heap. 

### Where are Heaps Used? 

