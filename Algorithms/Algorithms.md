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

## Asymptotic Analysis

There are many ways to solve a problem and therefore it is natural to compare alternatives. In this section, we will look at different techniques to determine which algorithm is better. 

When it comes to comparison, there are two things to keep in mind: **time** and **space**. The time corresponds to the amount of time an algorithm takes to solve the problem and space corresponds to the amount of memory the algorithm takes when solving the problem. 

Let's look at the time comparison first

### Comparing Execution Time

The execution time can easily be compared by running the algorithms on the computer and noting the duration each algorithm takes. However, the speed at which the algorithms run may differ based on the hardware the computer has. Thus the result may vary from computer to computer. Instead, an analytical evaluation is better suited for such comparison. 

#### Analytical Evaluation

In order to evaluate an algorithm analytically, we do the following: 

*   Consider a specific input size. Generally, this is set at $n$. 
*   Compute the number of **primitive operations** executed by an algorithm for the given input

When we follow these steps, we judge the algorithm that takes the least amount of 

#### Primitive Operations

Before we count the primitive operations, we need to understand what these operations really are. Primitive operations are operations that are implemented as processor instructions. These include assignment of a variable, array indexing, comparing variables, arthmetic operations, a function call, etc...

Operations such as printing the entire array is not considered a primitive operations. However, printing a single value is considered a primitive operation. The other thing to keep in mind is that when a function is called, all the statements in the function are executed. So, we cannot considered a function call as a single primitive operation but multiple. 

Conditional statements is also a primitive operation. However, the number of times they are executed is important to keep in mind. The conditional statements are a little tricky because depending on whether the condition is satisfied or not, the statement may or may not execute. So, how do we decide the number of primitive operations in such a case? 

In order to determine the primitive operations, we consider the: 

*   **Best case analysis** - In this case, given a specific input we look at the fewest number of primitive operations. This gives us the **lower bound** to the algorithm
*   **Worst case analysis** - In this case, given a specific input we look at the maximum number of primitive operations. This gives us the **upper bound** to the algorithm. 
*   **Average case analysis** - In this case, we compute the weighted average of the number of primitive operations executed for each input. 

In practice, we make use of the worst-case analysis. This allows us to keep an upper bound and not be surprised by the result. 

#### Analyzing a Simple Python Program

Let's consider an example to illustrate the time complexity of an algorithm. 

```python
x = 0
x += 1
print(x)
```

In this case, we see the following: 

![image-20201101104555116](Algorithms.assets/image-20201101104555116.png)

Thus these three lines constitute 6 primitive operations. Thus the time complexity for the above program is 6. Note that there is notion of input size here as there is no input. 

### Measuring Time Complexity

Let's consider another example to illustrate the measurement of time complexity. 

```python
n = 10
sum = 0
for var in range(10):
    sum += 1
    
print(sum)
```

So, what is the time complexity in this case: 

<img src="Algorithms.assets/image-20201101105354266.png" alt="image-20201101105354266" style="zoom:50%;" />

So, that would be: 

$1 + 1 + [n + (1 + 1+ ... +  1) + 3n] + 1 = 3+ [n + n + 3n] = 5n + 3$

>   Though `range(n)` executes only once, its execution cost is $n$ because each call to `range(n)` results in $n$ individual operations.

Let's consider another more complex example: 

```python
n = 5
sum = 0
for i in range(n):
    for j in range(n):
        sum += 1
        
print(sum)
```

 $1 + 1 + n + n + n[n + n + 3n] + 1$ = $3 + 2n + 5n^2$

Note that the first n corresponds to `range(n)` while the second $n$ corresponds to assignment in the first loop. The third $n[...]$ corresponds to inner loop being run 

### Asymptotic Analysis & Big O

As we saw in the previous section, the analysis of algorithms can be expressed in terms of a polynomial. However, such an analysis will become cumbersome as we get into complex algorithms. Instead, we resort to something quite simple. 

### Asymptotic Analysis 

When our input variable, $n$, is small, the comparison between two algorithms may not make sense. However, when $n$ becomes large it can make a difference. The analysis that is done when $n$ is large is called **asymptotic**. In this case, given two function $f(n)$ and $g(n)$, the asymptotic analysis compares two functions as $n$ increases. In the next few sections we will see come into play. 

#### Big O Notation

The Big O notation (pronounced Big Oh Notation) is as follows

>   A function $f(n)$ is considered $O(g(n))$ if there exists some positive real constant $c$ and an integer $n_o \geq 0$ such that the following inequality holds for all $n \geq n_0$: 
>   $$
>   f(n) \leq cg(n)
>   $$

The following graph shows the inequality: 

![image-20201102093348787](Algorithms.assets/image-20201102093348787.png)

The above inequality does not have to hold for all $n$. In other words, for $ n < n_0$, $f(n)$ is allowed to exceed $cg(n)$, but for all values of $n$ beyond some value $n_0$, $f(n)$ is not allowed to exceed $cg(n)$. 

Consider an example of an algorithm's time complexity to be $3n^3 + 4n + 2$. We can write this as an inequality: 

$3n^3 +4n + 2 \leq 9n^3 = O(n^3)$

This holds true beyond $n=2$. However, we know for sure that $O(n^2)$ or even $O(n)$ will not be true for any given $n$. But $O(n^4)$ or $O(n^5)$ will always be true. We can always find higher orders for which the inequality holds, but it would not make sense. Instead, it helps to see if the inequality holds for some constant times the largest power of the input. 

>   Suppose algorithm A and B have running time of $O(n)$ and $O(n^2)$, respectively for sufficiently large input sizes, algorithm A will run faster than algorithm B. That does not mean that algorithm A will always run faster than algorithm B. 

#### Simplified Asymptotic Analysis

Once we have obtained the complexity of an algorithm by counting the number of primitive operations, we can arrive at the Big O notation for the algorithm by: 

1.  dropping the multiplicative constants with all terms
2.  dropping all but the highest order term

For example, we can write: 

*   $n^2 + 2n + 1$ as $O(n^2)$
*   $n^5 + 2n + 43$ as $O(n^5)$

#### A comparison of some common functions

The table below shows the typical 12 functions that are used for comparison of asymptotic analysis: 

![image-20201102094901516](Algorithms.assets/image-20201102094901516.png)

The plot below illustrates some of these functions: 

![image-20201102094929622](Algorithms.assets/image-20201102094929622.png)

### Useful Formulas to help with Calculations

Below are some handy tables used for calculating time complexity of an algorithm: 

![image-20201102095244243](Algorithms.assets/image-20201102095244243.png)

Some of the formulas dealing with logarithmic expressions: 

![image-20201102095314288](Algorithms.assets/image-20201102095314288.png)

Few things to keep in mind: 

*   Every time a list or an array gets iterated over $c \times length$ times, it is most likely in $O(n)$ time.
*   When you see a problem where the number of elements in the problem space get halved each time, that will most probably be in $O(log n)$. 
*   Whenever you have a singly nested loop, the problem is most likely in $O(n^2)$

#### Common Complexity Scenarios

In this lesson we will see the most common examples and handly formulas for solving time complexity problems. 

##### Simple Loop

```python
for x in range(n):
    # Statements
```

The running complexity is $O(n)$ because the `range()` function which has $O(1)$ is called $n$ times. 

##### Loop with Increment

```python
for x in range(1, n, k):
    # Statements
```

The running complexity is $O(n)$

##### Simple Nested Loop

```python
for i in range(n):
    for j in range(m):
        # Statements
```

The running complexity is $O(nm)$. 

##### Nested for loop with dependent variables

```python
for i in range(n):
    for x in range(i):
        # Statements
```

