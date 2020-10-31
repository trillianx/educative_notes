[TOC]



# Algorithms

With algorithms being one of the most common themes in coding interviews, having a firm grip on them can be the difference between being hired and not. After completing this comprehensive course, you'll have an in-depth understanding of different algorithm types in Python and be equipped with a simple process for approaching complexity analysis. 

As you progress, you’ll be exposed to the most important algorithms you'll likely encounter in an interview. You'll work your way through over 50 interactive coding challenges and review detailed solutions for each problem. You’ll walk away with the ability to build-up to the optimal solution for addressing those tough coding interview questions head-on. 

In this course, you will learn about:

-   Major algorithmic paradigms
-   Measuring time complexities of algorithms
-   Searching and sorting in different data structures
-   Graphs, graph traversals, and other important graph algorithms
-   Greedy algorithms
-   The dynamic programming technique to efficiently solve problems
-   The divide and conquer method, i.e. solving multiple subparts of a problem to solve the bigger problem

## Algorithm Paradigms

There are different algorithm paradigms. We will list out some of the major ones used in coding interviews. 

### Brute Force

The brute force method is the most simple. It requires us to go through all of the possibilities to find solution to the problem we want to solve. Consider an example of finding the maximum, minimum, or a certain element in the list. The brute force approach requires us to go through each of the element in the list. 

#### Example: Linear Search

We are given an unsorted array. We wish to find a certain element. Suppose we wish to find the element, `9` in the array: 

![image-20201031110137897](Algorithms.assets/image-20201031110137897.png)

We would then loop through each element in the array, comparing the element with `9` at each step. The function would be: 

```python
def find_element(arr, valule):
    if len(arr) == 0:
        return -1
    for e in arr:
        if e == value:
            return 1
    return -1
```

Let's write a function to find the maximum value in the array: 

```python
def find_max(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    max_val = arr[0]
    for e in arr[1:]:
        if e > max_val:
            max_val = e
    return max_val
```

Let's write a function to find the minimum value in the array: 

```python
def find_min(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    min_val = arr[0]
    for e in arr[1:]:
        if e < min_val:
            min_val = e
    return min_val
```

In all of these functions, you will notice that we go through each of the elements. Therefore, the time complexity of these functions is $O(n)$. 

The **advantage** of brute force method is that we will always find a solution while the **disadvantage** is that such a solution may be inefficient.

### Greedy Algorithms

Greedy algorithms build up a solution, piece by piece. This means that it chooses the next piece that offers the most obvious and immediate benefits. The algorithm is called greedy because the choice the algorithm makes is the best at instance of time. The choice is **locally optimal** rather than **globally optimal**. 

>    If you have a problem where the locally-optimal choice leads to a global solution, the best fit is the Greedy technique. 

The greedy method can solve a problem that satisfies the below-mentioned properties: 

*   **Greedy Choice Property:** A global optimum can be arrived at by selecting a local optimum. 
*   **Optimal substructure:** An optimal solution to the complete problem contains an optimal solution to subproblems. 

Greedy algorithms work by recursively constructing a set of pieces from the smallest possible constituent parts. 

Let's take an example. Given a tree, we wish to find the path that is the longest. 

![image-20201031112219830](Algorithms.assets/image-20201031112219830.png)

The greedy algorithm starts at 7, which is the root node. It then compares the next node. As 3 < 12, it chooses the node 12. It again compares the next two nodes. As 5 < 6, it picks 6. Thus the longest path, according to the greedy algorithm is 25. However, the longest path is 109. By making localized choice that were optimal the greedy algorithm got the answer wrong. However, if the local decisions were optimally correct which resulted in global optimal, it would be have been correct. 

The **advantage** of greedy algorithm is that solutions to smaller instances of the problem can be straightforward and easy to understand. It works best when the optimal solution of the subset is the solution for the superset as well. 

The **disadvantage** of greedy algorithm is that sometimes the most optimal short-term solutions may lead to the worst possible solution to the whole problem. 

### Divide & Conquer

Divide and conquer is an algorithm that repeatedly divides a problem into subproblems until we reach a point where each problem is similar and atomic (i.e. it cannot be divided further). 

#### Example: Atomic Problem

Consider an example of an array that has upper and lower case letters. The task is to term them into lower case. We solve this problem by following these 3 steps: 

1.  **Divide**

    First break the problem at hand into smaller subproblems. This step can be achieved by dividing the list containing the alphabets into subsets until a single unit is left and no further division is possible. 

    ![image-20201031114112526](Algorithms.assets/image-20201031114112526.png)

2.  **Conquer**

    Solve the received atomic subproblems from step 1. Often, the problems are considered solved and passed onto the next step. 

    ![image-20201031114237063](Algorithms.assets/image-20201031114237063.png)

3.  **Merge**

    Repeatedly combine the solved subproblems to formulate a solution for the original problem

    ![image-20201031114333275](Algorithms.assets/image-20201031114333275.png)

#### Advantages: 

*   It can be optimal for a general case solution whwere the problem is easy to divide and the subproblem at some level is easy to solve.
*   It makes efficient use of memory cache because, when the problem gets divided into subproblems, it becomes smaller enough to be easily solved in the cache itself. 

#### Disadvantages: 

*   It uses recursive approach. In general, a recursive approach is slow and takes more space. 
*   Sometimes dividing the problem will not result in an optimal solution. For example, dividing the numbers before summing them is less efficient than summing them iteratively. 

### Dynamic Programming

Dynamic programming algorithms solve problems by combining results of subproblems--just like divide and conquer algorithms. 

Here are some characteristics: 

1.  **Overlapping Subproblems:** the subproblems of a given problem are not independent. In other words, two subproblems share a problem. 
2.  **Optimal Substructure Property:** the overall optimal solution of the problem can be constructed from the optimal solutions of its subproblems

#### Dynamic Programming Patterns

There are two approaches which are used to solve: 

##### Memoization (top down)

This approach is similar to recursion version except it looks for the answer of a subproblem in a lookup table before computing its solution

##### Tabulation (bottom-up)

Tabulation is the opposite of the top-down approach and it avoids recursion. In this approach, we fill the lookup table and computing the solution to the original problem based on the results in the table.

*   Dynamic programming speeds up the recursion technique and uses much less code.
*   Dynamic programming takes a lot of memory to store the calculated result of every subproblem. 
*   There is no general form for problems solved by dynamic programming. Every problem has to be solved in its own way. 