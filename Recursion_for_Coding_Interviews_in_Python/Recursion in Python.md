[TOC]



# Recursion for Coding Interviews in Python

If you’ve ever struggled with solving coding problems using recursion, or if you need to brush up your recursion skills for an interview, this course is for you! We will start with the basics of recursion before we practice solving actual coding problems. By the time you have completed this course, you’ll be able to use all the concepts of recursion to solve complex, real-world problems. 

## Chapter 1: Recursion Fundamentals

Recursion occurs when a function calls itself repeatedly until it reaches a specific stopping condition. Such a function is called a **recursive function**. 

>   Recursion is the process of describing an action in terms of itself

The reason we wish to use recursion because: 

*   Tasks that are composed of similar subtasks
*   Shorter and easier code
*   Loops converted to recursive by compiler

### Format of Recursive Function

A recursive function consists of two main parts: 

*   **Base Case:** is where all further calls to the same function stop
*   **Recursive Case:** is where the function calls itself repeatedly until it reaches the base case

The syntax of a recursive function is the following: 

```python
def RecursiveFunction():
    # Base Case
    if <baseCaseCondition>:
        return <some base case value>
    # Recursive Case
    else:
        return (recursive call and any other task)
```

The base case leads to returning values while the recursive case always calls the function again along with some values

### Recursion & Memory Visualization

Let’s look at how memory is allocated in recursion. When a function is called, its memory is allocated on a **stack**. A stack is a LIFO (Last-In-First-Out) process. When a function executes, it adds its state data to the top of the stack. When a function exits, this data is removed from the stack. 

Suppose we have a function: 

```python
def function1(<parameters>) :
  <create some variables>
  return(<some data>)
 
def function2(<parameters>) :
  <create some variables>
  return(<some data>)
 
# Driver Code
function1()
function2()
```

The memory stack will now look like this: 

<img src="Recursion%20in%20Python.assets/image-20201005102227436.png" alt="image-20201005102227436" style="zoom:30%;" />

A recursive function calls itself, so the memory for a called function is allocated on top of the memory allocated for **calling the function**. When the function reaches the base case, the value of the base case is returned, its memory is de-allocated and the process continues in reverse until all the functions are returned. 

To illustrate this, let’s look at an example of a factorial function. The factorial function is recursive because a factorial of a number is simply the product of all the numbers before it until we reach 1. 

```python
def factorial(n):
    if n < 0: 
        return 'Invalid number'
    # Base Case
    if n <= 1:
        return 1
    # Recursive Case
    else:
        return n * factorial(n-1)
```

Now let’s call the function: 

```python
factorial(5)

120
```

We can visualize this as follows: 

<img src="Recursion%20in%20Python.assets/image-20201005103116999.png" alt="image-20201005103116999" style="zoom:33%;" />

Running through each we stack the function on top of each other: 

<img src="Recursion%20in%20Python.assets/image-20201005103159624.png" alt="image-20201005103159624" style="zoom:33%;" />

Until we reach the top. The function `factorial(1)` is the base case which returns the value of 1. That value is then multiplied by the return of the function `factorial(2)` and so forth. Until we get to the final call in the stack. 

This can also be visualized it in the following way: 

<img src="Recursion%20in%20Python.assets/image-20201005103403769.png" alt="image-20201005103403769" style="zoom:33%;" />

Once the base case is reached, we then get: `2 * 1 = 2` followed by `3 * 2 = 6`, then `4 * 6 = 24` and ending with `24 * 5= 120`, the answer. 

### Direct Vs Indirect Recursion

In this section we will go over two types of recursions. Let’s look at each one of them: 

#### Direct Recursion

Direct recursion occurs when a function calls itself, in the sense, the function makes a recursive call inside its own function body. This is what we have seen in the factorial example. 

In general, the synax is: 

```python
def function1():
    # Some code
    function1()
```



Let’s consider another example. Without using a loop print natural numbers from 1 to n using direct recursion: 

```python
def natural_numbers(n):
    if n < 0:
        return "Invalid Number"
    # Base Case: 
    if n <= 1: 
        print(1)
    # Recursive Case:
    else:
        natural_numbers(n-1)
        print(n)
```

Note that we did not make use of the `return` statement here. We see here that until the base case is reached, nothing is printed to the screen. But when it begin to unstack, we start printing the numbers. This is easily visualized by looking at the function that prints in reverse: 

```python
def natural_numbers(n):
    if n < 0:
        return "Invalid Number"
    # Base Case: 
    if n <= 1: 
        print(1)
    # Recursive Case:
    else:
        print(n)
        natural_numbers(n-1)
```

In this case, the `print(n)` is executed as we stack the function calls. So, we print the number and we stack the recursive call, `natural_numbers(n-1)`. So, the order matters. 

>   If a statement is after the function call in a recursive function, it will be executed when we begin to de-stack. 
>
>   If the statement is before the recursive call, it will be executed when we begin to stack. 

#### Indirect Recursion

Indirect recursion occurs when a function calls another function until the original function is called again. The general syntax is: 

```python
def function1():
    function2()
    
def function2():
    function1()
```

### When to Use Recursion

Even though recursion may seem like a good idea to use all the time, there are times when recursion is not a good idea. 

Recursion should be used where it just feels natural. This will become obvious as you continue to work on various recursion problems. The most obvious indications of recursion are:

*   when the problem can be broken down into **smaller subproblems**. It is likely that a problem can be solved using recursion when you observe a pattern of that problem breaking down into similar subproblems. 
*   When a problem requires an absurd number of nested loops. When the number of nested loops are known, use iteration but when we do not know the number of loops, stick to recursion. 

### Understanding a Recursive Problem

In this section, we will go over methods to help you visualize a recursive function. Let's consider another problem. We are interested in printing the following sequence: 

```python
10
5
0
5
10
```

Let's write down a function that creates such a pattern:

```python
def printPattern(targetNumber):
    if targetNumber <= 0:
        print(0)
    else:
        print(targetNumber)
        printPattern(targetNumber-5)
        print(targetNumber)
```

So, we see that the first print statement prints the values before the recursion call goes into the stack while the second one is printed after we de-stack. 